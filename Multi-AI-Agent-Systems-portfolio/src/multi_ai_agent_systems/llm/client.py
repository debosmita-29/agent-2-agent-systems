from __future__ import annotations

import httpx

from multi_ai_agent_systems.config import settings


class LLMClient:
    async def complete(self, system_prompt: str, user_prompt: str) -> str:
        provider = settings.llm_provider.lower().strip()

        if provider == "openai":
            return await self._openai(system_prompt, user_prompt)
        if provider == "anthropic":
            return await self._anthropic(system_prompt, user_prompt)
        if provider == "ollama":
            return await self._ollama(system_prompt, user_prompt)

        return self._rule_based()

    def _rule_based(self) -> str:
        return (
            "I routed the request to the right agents, created the required tasks, "
            "updated memory, and prepared the next-step plan. Configure OpenAI, Claude, "
            "or Ollama for richer synthesis."
        )

    async def _openai(self, system_prompt: str, user_prompt: str) -> str:
        if not settings.openai_api_key:
            raise RuntimeError("OPENAI_API_KEY is required when LLM_PROVIDER=openai")

        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(
                "https://api.openai.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {settings.openai_api_key}"},
                json={
                    "model": settings.openai_model,
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                    "temperature": 0.2,
                },
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]

    async def _anthropic(self, system_prompt: str, user_prompt: str) -> str:
        if not settings.anthropic_api_key:
            raise RuntimeError("ANTHROPIC_API_KEY is required when LLM_PROVIDER=anthropic")

        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(
                "https://api.anthropic.com/v1/messages",
                headers={
                    "x-api-key": settings.anthropic_api_key,
                    "anthropic-version": "2023-06-01",
                    "content-type": "application/json",
                },
                json={
                    "model": settings.anthropic_model,
                    "max_tokens": 1000,
                    "system": system_prompt,
                    "messages": [{"role": "user", "content": user_prompt}],
                },
            )
            response.raise_for_status()
            return "\n".join(
                block.get("text", "") for block in response.json()["content"] if block.get("type") == "text"
            )

    async def _ollama(self, system_prompt: str, user_prompt: str) -> str:
        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(
                f"{settings.ollama_base_url}/api/chat",
                json={
                    "model": settings.ollama_model,
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                    "stream": False,
                },
            )
            response.raise_for_status()
            return response.json()["message"]["content"]
