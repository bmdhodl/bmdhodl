<div align="center">

### Patrick Hughes

**Manager of Software Engineering & AI @ OneOncology**

Building AI-operated systems out of Nashville, TN

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/patrickhughes013)
[![Blog](https://img.shields.io/badge/bmdpat.com-111111?style=flat-square&logo=About.me&logoColor=white)](https://bmdpat.com)
[![PyPI](https://img.shields.io/pypi/v/agentguard47?style=flat-square&color=3776AB&label=agentguard47%20on%20PyPI)](https://pypi.org/project/agentguard47)

</div>

---

Day job: engineering + AI at a healthcare company.

After hours: running **BMD HODL** -- a one-person AI-operated holding company. 12 agents. One human. Compound across decades.

---

## Open Source

### [AgentGuard](https://github.com/bmdhodl/agent47) &nbsp; `pip install agentguard47`

Your agent just burned $200. AgentGuard stopped it at $5.

Runtime cost guardrails for AI agents. Budget caps, loop detection, kill switches. Drop it in front of any LLM call. Zero dependencies. MIT.

```python
from agentguard47 import AgentGuard

guard = AgentGuard(budget=5.00)

with guard:
    response = client.chat(...)  # enforces budget at runtime
```

Works with OpenAI, Anthropic, LangChain, or anything that makes LLM calls.

---

## Stack

```
Python, TypeScript, Next.js, Supabase, Vercel
Claude API + OpenAI + llama.cpp
Local inference: RTX 3070 + RTX 5070 Ti + RTX 5090 (Llama 3.1 8B)
```

---

## Writing

I write about AI agents, local LLMs, and building things solo.

Recent posts at [bmdpat.com](https://bmdpat.com):
- [Prompt injection and AI agents: what actually breaks](https://bmdpat.com/blog/prompt-injection-ai-agents-business-guide-2026)
- [Local LLM inference on consumer GPUs in production](https://bmdpat.com/blog/local-llm-inference-consumer-gpu-production-2026)
- [AI agent cost control with AgentGuard](https://bmdpat.com/blog/ai-agent-cost-control-agentguard-python)

---

<div align="center">

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=bmdhodl&show_icons=true&theme=dark&hide_border=true&count_private=true&include_all_commits=true)

</div>
