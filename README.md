<div align="center">

# Patrick Hughes

### Building BMD HODL, a one-person AI-operated holding company. Nashville, TN.

Agents write the code, run the tests, and open the PRs. I set the goals and read the receipts.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/patrickhughes013)
[![Blog](https://img.shields.io/badge/bmdpat.com-111111?style=for-the-badge&logo=About.me&logoColor=white)](https://bmdpat.com)
[![X](https://img.shields.io/badge/@phughes9000-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/phughes9000)
[![PyPI](https://img.shields.io/pypi/v/agentguard47?style=for-the-badge&color=3776AB&label=agentguard47&logo=pypi&logoColor=white)](https://pypi.org/project/agentguard47)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white)](https://nextjs.org/)
[![Anthropic](https://img.shields.io/badge/Claude_API-CC785C?style=for-the-badge&logo=anthropic&logoColor=white)](https://anthropic.com/)
[![Supabase](https://img.shields.io/badge/Supabase-3FCF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com/)
[![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://vercel.com/)
[![NVIDIA](https://img.shields.io/badge/RTX_5090-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://nvidia.com/)

</div>

---

## Open Source

### [AgentGuard](https://github.com/bmdhodl/agent47) &nbsp; `pip install agentguard47`

Your agent just burned $200. AgentGuard stopped it at $5.

Runtime cost guardrails for AI agents: budget caps, loop detection, kill switch. Drop it in front of any LLM call. Zero dependencies. MIT.

```python
from agentguard47 import AgentGuard

guard = AgentGuard(budget=5.00)

with guard:
    response = client.chat(...)  # enforced at runtime
```

Works with OpenAI, Anthropic, LangChain, or anything that makes LLM calls.

### [showwork](https://github.com/bmdhodl/showwork)

"Done" is a claim. showwork makes agents prove it: falsifiable claims checked deterministically, refused when reality disagrees. Not observability. Proof. Every repo in my fleet closes through it.

### [render-first-ocr](https://github.com/bmdhodl/render-first-ocr)

Offline, CPU-only PDF OCR. Rasterize every page, OCR the pixels, treat embedded text as a hint and never as truth. Tesseract + RapidOCR, bounded retries, atomic JSONL output. MIT.

### [mib-doc-solution](https://github.com/bmdhodl/mib-doc-solution)

Air-gapped document-intake pipeline for the 8090 MIB Doc Challenge. Scored 137.23/150 on the public train set with zero catastrophic false approvals.

---

## Local AI Rig

```
RTX 5090 + RTX 5070 Ti + RTX 3070
llama.cpp · measured, not guessed
```

I benchmark local models on this hardware and publish the numbers: tokens per second, wall clock, watts, refusal rates. The sizing desk at [bmdpat.com/desk](https://bmdpat.com/desk) runs on that data.

---

## Writing

Measured local-LLM data and agent-fleet notes at [bmdpat.com](https://bmdpat.com):

- [My local models refused zero of 50 security tasks](https://bmdpat.com/blog/local-llm-refusal-rate-security-tasks-2026)
- [The faster local model run took 83x longer](https://bmdpat.com/blog/local-llm-tokens-per-second-wall-clock-2026)
- [Why local LLM benchmarks need power data](https://bmdpat.com/blog/local-llm-benchmark-power-data-2026)

---

<div align="center">

![Profile Views](https://komarev.com/ghpvc/?username=bmdhodl&color=3776AB&style=for-the-badge)

</div>
