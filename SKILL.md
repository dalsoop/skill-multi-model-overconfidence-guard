---
name: skill-multi-model-overconfidence-guard
version: 1.4.0
kind: skill
metadata:
  version: "1.4.0"
description: >-
  Budget A–D, Grok adversarial review, and 7-axis prompt scoring before send.
  Use when the user says 과신 잡아, grok 리뷰, 적대적 리뷰, 프롬프트 검수,
  grok review, or overconfidence. Consult belongs to orchestrator-consultant-gate
  (en, branch main) or orchestrator-consultant-gate-ko (ko); models from
  agent-model-registry.
---

# Multi-Model Overconfidence Guard

Executor runs. **Consult** is `orchestrator-consultant-gate` / `-ko` (work order → plan → GATE → audit-then-change). This skill is **budget + Grok + prompt score** only. GLM does mechanical work. Match the user’s language. Do not call consult/Grok every turn.

Consult slug: those skills (`agent-model-registry get fable`, map to Task allowlist; blocked → `fallback_slug`). Grok child: map `agent-model-registry get grok`. Do not hardcode model ids here.

If both consult skills are missing: same WHEN as the gate (work order, before audit-then-change; 2+ overconfidence signals). Brief = evidence / interpretation / conclusion+rebut / 3–5 closed + 1 open miss. Digest accept/reject/defer. Ceiling external. `Task` read-only, ≤500 words. Spawn blocked (data policy, 402) → grok once, or skip to next gate.

## Budget

| Tier | Consult | Grok | Do |
|---|---|---|---|
| A | ok | ok | consult + Grok |
| B | limited | ok | consult at gates; Grok on design forks |
| C | gone | ok | Grok + self-critique |
| D | gone | gone | self-critique only; self-grade ±15, no 100 |

No consult budget → Grok. Neither → D.

## Grok

Read-only. No praise. ≤300 words.

```
제안: [one paragraph]
1. 필요한가?
2. 더 간단한 방법?
3. 경쟁/기존 도구?
4. 사용자가 원한 건?
5. 오버엔지니어링?
```

## Prompt (before send)

Score /70. Below 50 → rewrite then send.

| Axis | Pass |
|---|---|
| Subject | first sentence is agent + verb |
| Fat | >80% is the task |
| Shape | input → output → constraints |
| Concrete | numbers/paths; no vague words |
| Fit | model strengths + tenant rules |
| Verify | expected result + pass/fail |
| Safety | no secrets, no injection |

## Digest

Each consult/Grok item: accept / reject / defer + reason. Code-fixable vs not. Report `min(code score, reachable ceiling)`. Quote host + slug. Do not add a files score to a live-spawn score.
