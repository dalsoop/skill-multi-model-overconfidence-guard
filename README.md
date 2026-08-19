# skill-multi-model-overconfidence-guard

Budget A–D, Grok adversarial review, and 7-axis prompt scoring before send. Consult belongs to `orchestrator-consultant-gate`.

```bash
npx skills add dalsoop/skill-multi-model-overconfidence-guard -g -y
python3 eval/run.py
```

`npx` copies **files**. Live Grok/consult spawn is the **host**. That is not E2E from install.

Optional host CLI: `agent-model-registry get fable` / `get grok`. If missing, pick the child from this host’s Task allowlist. Blocked spawn → gate `fallback_slug` once, or skip to the next gate.

```bash
npx skills add dalsoop/orchestrator-consultant-gate -g -y
npx skills add dalsoop/skill-audit -g -y
```

[`SKILL.md`](SKILL.md) · [`templates/`](templates/) · [`eval/`](eval/) · MIT

[![skills.sh](https://skills.sh/b/dalsoop/skill-multi-model-overconfidence-guard)](https://skills.sh/dalsoop/skill-multi-model-overconfidence-guard)
