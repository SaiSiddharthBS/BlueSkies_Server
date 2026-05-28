# AI Rate Limit Monitor - Unbiased Execution Blueprint

## 1. The Core Architecture
**Format:** Google Chrome / Edge Browser Extension (Manifest V3)
**Reasoning:** A standalone desktop app (like Python/Electron) was strictly rejected because it cannot legally inject into Chrome to track ChatGPT web limits, and it suffers from massive CORS blockades when pinging APIs natively.

## 2. Web Browser Subscriptions (ChatGPT Plus, Claude Pro)
**Method:** Passive DOM / network XHR Interception
**How it works:** The extension sits passively in the browser. When the user types on `chatgpt.com`, the extension silently intercepts the backend XHR requests locally, physically counting message decrements. It does not require passwords or break Terms of Service.

## 3. Developer API Keys (Anthropic, OpenAI, Gemini)
**Method:** The "1-Token Micro-Ping" Protocol
**How it works:** 
1. The user pastes their API keys strictly into the extension's secure local vault (`chrome.storage.local`). They are never uploaded to our servers.
2. The extension uses `host_permissions` to entirely bypass browser CORS security blocks.
3. The extension checks limits purely On-Demand (No background looping/draining!). It pings the cheapest available tier (e.g., Claude Haiku) for exactly `1 max_token` ("A"). This costs exactly `$0.000000375` per check and perfectly fetches the official rate-limit headers mathematically returning from the AI servers.

## UI / UX Limitations & Design
- **Rejected:** Floating desktop widgets (massively distracting).
- **Approved:** A high-end, sleek, dark-glassmorphic dropdown popup menu that clicks out from the browser's extension bar. It contains two seamlessly unified tabs: `[Web Subscriptions]` and `[API Keys]`.
