(() => {
  "use strict";

  const REPO = "https://github.com/4i7/Denno-Watch";
  const CATEGORY_LABELS = {
    incident: "INCIDENT",
    analysis: "ANALYSIS",
    methodology: "REFERENCE",
  };
  const STATUS_LABELS = {
    draft: "Draft",
    confirmed: "確認済み",
    investigating: "調査中",
    under_investigation: "調査中",
    restored: "復旧済み",
    restored_with_remediation_followup: "復旧・是正継続",
    service_restored_monitoring: "復旧・監視中",
    contained_investigation_ongoing: "封じ込め・調査継続",
    containment_complete: "封じ込め済み",
    recovery_ongoing: "復旧中",
    public_investigation_complete: "公表上の調査完了",
  };

  const els = {
    results: document.querySelector("#results"),
    template: document.querySelector("#document-card-template"),
    search: document.querySelector("#search-input"),
    year: document.querySelector("#year-filter"),
    status: document.querySelector("#status-filter"),
    sort: document.querySelector("#sort-filter"),
    resultCount: document.querySelector("#result-count"),
    resultContext: document.querySelector("#result-context"),
    activeTags: document.querySelector("#active-tags"),
    empty: document.querySelector("#empty-state"),
    error: document.querySelector("#load-error"),
    reset: document.querySelector("#reset-filters"),
    generatedAt: document.querySelector("#generated-at"),
    theme: document.querySelector("#theme-toggle"),
    metricIncidents: document.querySelector("#metric-incidents"),
    metricAnalysis: document.querySelector("#metric-analysis"),
    metricMethodology: document.querySelector("#metric-methodology"),
    metricTotal: document.querySelector("#metric-total"),
  };

  const state = {
    query: "",
    category: "all",
    year: "all",
    status: "all",
    sort: "updated-desc",
    tag: null,
  };

  let catalog = null;

  function safeText(value) {
    return value == null ? "" : String(value);
  }

  function normalise(value) {
    return safeText(value).normalize("NFKC").toLocaleLowerCase("ja-JP").trim();
  }

  function dateLabel(value) {
    if (!value) return "更新日不明";
    const match = safeText(value).match(/^(\d{4})-(\d{2})-(\d{2})/);
    if (match) return `${match[1]}.${match[2]}.${match[3]}`;
    const date = new Date(value);
    if (Number.isNaN(date.getTime())) return safeText(value);
    return new Intl.DateTimeFormat("ja-JP", {
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
    }).format(date);
  }

  function statusValue(doc) {
    return doc.incident?.incidentStatus || doc.status || "unknown";
  }

  function statusLabel(value) {
    const text = safeText(value);
    return STATUS_LABELS[text] || text.replaceAll("_", " ");
  }

  function sourceUrl(path) {
    const encoded = safeText(path)
      .split("/")
      .map((part) => encodeURIComponent(part))
      .join("/");
    return `${REPO}/blob/main/${encoded}`;
  }

  function populateFilters(data) {
    for (const year of data.years || []) {
      const option = document.createElement("option");
      option.value = String(year);
      option.textContent = String(year);
      els.year.append(option);
    }

    const statuses = [...new Set(data.documents.map(statusValue).filter(Boolean))].sort();
    for (const status of statuses) {
      const option = document.createElement("option");
      option.value = status;
      option.textContent = statusLabel(status);
      els.status.append(option);
    }
  }

  function loadStateFromUrl() {
    const params = new URLSearchParams(location.search);
    const category = params.get("category");
    const sort = params.get("sort");
    state.query = params.get("q") || "";
    state.category = ["all", "incident", "analysis", "methodology"].includes(category)
      ? category
      : "all";
    state.year = params.get("year") || "all";
    state.status = params.get("status") || "all";
    state.sort = ["updated-desc", "year-desc", "title-asc"].includes(sort)
      ? sort
      : "updated-desc";
    state.tag = params.get("tag") || null;
  }

  function syncControls() {
    els.search.value = state.query;
    els.year.value = [...els.year.options].some((o) => o.value === state.year)
      ? state.year
      : "all";
    state.year = els.year.value;
    els.status.value = [...els.status.options].some((o) => o.value === state.status)
      ? state.status
      : "all";
    state.status = els.status.value;
    els.sort.value = state.sort;
    document.querySelectorAll("[data-category]").forEach((button) => {
      button.classList.toggle("is-active", button.dataset.category === state.category);
      button.setAttribute("aria-pressed", button.dataset.category === state.category ? "true" : "false");
    });
  }

  function updateUrl() {
    const params = new URLSearchParams();
    if (state.query) params.set("q", state.query);
    if (state.category !== "all") params.set("category", state.category);
    if (state.year !== "all") params.set("year", state.year);
    if (state.status !== "all") params.set("status", state.status);
    if (state.sort !== "updated-desc") params.set("sort", state.sort);
    if (state.tag) params.set("tag", state.tag);
    const query = params.toString();
    history.replaceState(null, "", `${location.pathname}${query ? `?${query}` : ""}${location.hash}`);
  }

  function filteredDocuments() {
    const terms = normalise(state.query).split(/\s+/).filter(Boolean);
    let docs = catalog.documents.filter((doc) => {
      if (state.category !== "all" && doc.category !== state.category) return false;
      if (state.year !== "all" && String(doc.year || "") !== state.year) return false;
      if (state.status !== "all" && statusValue(doc) !== state.status) return false;
      if (state.tag && !(doc.tags || []).includes(state.tag)) return false;
      if (terms.length && !terms.every((term) => normalise(doc.searchText).includes(term))) return false;
      return true;
    });

    docs = [...docs].sort((a, b) => {
      if (state.sort === "title-asc") {
        return safeText(a.title).localeCompare(safeText(b.title), "ja");
      }
      if (state.sort === "year-desc") {
        return (b.year || 0) - (a.year || 0) || safeText(b.updatedAt).localeCompare(safeText(a.updatedAt));
      }
      return safeText(b.updatedAt).localeCompare(safeText(a.updatedAt)) || (b.year || 0) - (a.year || 0);
    });
    return docs;
  }

  function appendFact(dl, label, value) {
    if (!value) return;
    const dt = document.createElement("dt");
    const dd = document.createElement("dd");
    dt.textContent = label;
    dd.textContent = safeText(value);
    dl.append(dt, dd);
  }

  function createCard(doc) {
    const card = els.template.content.firstElementChild.cloneNode(true);
    const category = card.querySelector(".category-badge");
    const year = card.querySelector(".year-badge");
    const freshness = card.querySelector(".freshness-badge");
    const title = card.querySelector("h3");
    const summary = card.querySelector(".card-summary");
    const facts = card.querySelector(".incident-facts");
    const tags = card.querySelector(".tag-list");
    const updated = card.querySelector(".updated-at");
    const link = card.querySelector(".source-link");

    category.textContent = CATEGORY_LABELS[doc.category] || safeText(doc.category).toUpperCase();
    if (doc.year) {
      year.textContent = String(doc.year);
    } else {
      year.hidden = true;
    }

    if (doc.staleAfter) {
      const staleDate = new Date(doc.staleAfter);
      if (!Number.isNaN(staleDate.getTime()) && staleDate.getTime() < Date.now()) {
        freshness.hidden = false;
        freshness.textContent = "RECHECK DUE";
        freshness.title = `再確認期限: ${dateLabel(doc.staleAfter)}`;
      }
    }

    title.textContent = doc.title || doc.path;
    summary.textContent = doc.summary || "概要は原文を参照してください。";

    if (doc.incident) {
      facts.hidden = false;
      appendFact(facts, "組織", doc.incident.organization);
      appendFact(facts, "類型", doc.incident.attackType);
      appendFact(facts, "公開状態", statusLabel(doc.incident.incidentStatus));
      appendFact(facts, "データ影響", doc.incident.dataExposure);
      appendFact(facts, "最終更新", dateLabel(doc.incident.latestPublicUpdate));
    }

    for (const tag of (doc.tags || []).slice(0, 7)) {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "tag-button";
      button.textContent = `#${tag}`;
      button.title = `${tag} で絞り込む`;
      button.addEventListener("click", () => {
        state.tag = tag;
        applyState({ scroll: true });
      });
      tags.append(button);
    }

    if (!tags.childElementCount) tags.hidden = true;
    updated.textContent = `更新: ${dateLabel(doc.updatedAt || doc.generatedAt)}`;
    link.href = sourceUrl(doc.path);
    link.setAttribute("aria-label", `${doc.title} を GitHub で開く`);
    return card;
  }

  function renderActiveTags() {
    els.activeTags.replaceChildren();
    if (!state.tag) return;
    const chip = document.createElement("button");
    chip.type = "button";
    chip.className = "filter-chip";
    chip.textContent = `#${state.tag} ×`;
    chip.title = "タグ絞り込みを解除";
    chip.addEventListener("click", () => {
      state.tag = null;
      applyState();
    });
    els.activeTags.append(chip);
  }

  function renderContext(docs) {
    const labels = [];
    if (state.query) labels.push(`「${state.query}」`);
    if (state.category !== "all") labels.push(CATEGORY_LABELS[state.category]);
    if (state.year !== "all") labels.push(`${state.year}年`);
    if (state.status !== "all") labels.push(statusLabel(state.status));
    if (state.tag) labels.push(`#${state.tag}`);
    els.resultContext.textContent = labels.length ? labels.join(" / ") : "全公開ナレッジ";
    els.resultCount.textContent = new Intl.NumberFormat("ja-JP").format(docs.length);
  }

  function render() {
    const docs = filteredDocuments();
    els.results.replaceChildren(...docs.map(createCard));
    els.results.setAttribute("aria-busy", "false");
    els.empty.hidden = docs.length !== 0;
    els.results.hidden = docs.length === 0;
    renderActiveTags();
    renderContext(docs);
  }

  function applyState({ scroll = false } = {}) {
    syncControls();
    updateUrl();
    render();
    if (scroll) {
      document.querySelector(".browser").scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }

  function applyPreset(preset) {
    state.query = preset.query ?? "";
    state.category = preset.category ?? "all";
    state.year = preset.year ?? "all";
    state.status = preset.status ?? "all";
    state.sort = preset.sort ?? "updated-desc";
    state.tag = preset.tag ?? null;
    applyState({ scroll: true });
  }

  function resetFilters() {
    applyPreset({});
  }

  function wireEvents() {
    let searchTimer;
    els.search.addEventListener("input", () => {
      clearTimeout(searchTimer);
      searchTimer = setTimeout(() => {
        state.query = els.search.value.trim();
        state.tag = null;
        applyState();
      }, 90);
    });

    els.year.addEventListener("change", () => {
      state.year = els.year.value;
      applyState();
    });
    els.status.addEventListener("change", () => {
      state.status = els.status.value;
      applyState();
    });
    els.sort.addEventListener("change", () => {
      state.sort = els.sort.value;
      applyState();
    });
    els.reset.addEventListener("click", resetFilters);

    document.querySelectorAll("[data-category]").forEach((button) => {
      button.addEventListener("click", () => {
        state.category = button.dataset.category;
        applyState();
      });
    });

    document.querySelectorAll("[data-preset-category]").forEach((button) => {
      button.addEventListener("click", () => {
        applyPreset({ category: button.dataset.presetCategory });
      });
    });

    document.querySelectorAll("[data-preset]").forEach((button) => {
      button.addEventListener("click", () => {
        try {
          applyPreset(JSON.parse(button.dataset.preset));
        } catch (error) {
          console.error("Invalid preset", error);
        }
      });
    });

    document.addEventListener("keydown", (event) => {
      const target = event.target;
      const typing = target instanceof HTMLInputElement || target instanceof HTMLTextAreaElement || target instanceof HTMLSelectElement;
      if (event.key === "/" && !typing) {
        event.preventDefault();
        els.search.focus();
      }
      if (event.key === "Escape" && document.activeElement === els.search && els.search.value) {
        els.search.value = "";
        state.query = "";
        applyState();
      }
    });
  }

  function setMetrics(data) {
    els.metricIncidents.textContent = data.counts?.incidents ?? 0;
    els.metricAnalysis.textContent = data.counts?.analysis ?? 0;
    els.metricMethodology.textContent = data.counts?.methodology ?? 0;
    els.metricTotal.textContent = data.counts?.documents ?? data.documents.length;
    els.generatedAt.textContent = data.generatedAt ? dateLabel(data.generatedAt) : "生成時刻不明";
  }

  function setupTheme() {
    const modes = ["auto", "light", "dark"];
    const labels = { auto: "自動", light: "ライト", dark: "ダーク" };
    const stored = localStorage.getItem("denno-watch-theme");
    const initial = modes.includes(stored) ? stored : "auto";
    document.documentElement.dataset.theme = initial;
    els.theme.title = `表示テーマ: ${labels[initial]}`;

    els.theme.addEventListener("click", () => {
      const current = document.documentElement.dataset.theme || "auto";
      const next = modes[(modes.indexOf(current) + 1) % modes.length];
      document.documentElement.dataset.theme = next;
      localStorage.setItem("denno-watch-theme", next);
      els.theme.title = `表示テーマ: ${labels[next]}`;
      els.theme.setAttribute("aria-label", `表示テーマ: ${labels[next]}`);
    });
  }

  async function init() {
    setupTheme();
    try {
      const response = await fetch("./catalog.json", { cache: "no-store" });
      if (!response.ok) throw new Error(`catalog: HTTP ${response.status}`);
      catalog = await response.json();
      if (!Array.isArray(catalog.documents)) throw new Error("catalog: invalid documents");
      populateFilters(catalog);
      loadStateFromUrl();
      setMetrics(catalog);
      wireEvents();
      applyState();
    } catch (error) {
      console.error(error);
      els.results.hidden = true;
      els.empty.hidden = true;
      els.error.hidden = false;
      els.generatedAt.textContent = "読み込み失敗";
      els.results.setAttribute("aria-busy", "false");
    }
  }

  init();
})();
