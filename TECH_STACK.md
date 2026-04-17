# FULL TECHNICAL STACK & ARCHITECTURE

This document details the exact technologies used to build the **Zero-Trust Insurance Operating System** (Aeterna Vault / Clamp). This is structured perfectly for your Hackathon slide deck and GitHub readme.

---

## 1. FRONTEND ARCHITECTURE (What we use & will use)

The frontend is designed to be a "Cyber-Luxury" WebGL interface, breaking away from standard HTML forms.

### Currently Implemented (What we use)
* **React.js**: The core component engine handling the state of the application (Microphone triggers, Fraud alerts, Verification Cards). We run this serverless via Babel for instant hackathon execution.
* **Three.js (WebGL)**: The 3D Engine used to construct the central Vault, the lighting physics, and the floating particle atmosphere.
* **GSAP (GreenSock Animation Platform)**: The mathematics library handling the cinematic animations (e.g., the 4 Quantum Bolts sliding into place, the vault swinging open).
* **Tailwind CSS**: Utility-first CSS using custom hex configurations (`Midnight Cobalt: #0A0F1E`, `Obsidian: #02040A`, `Gold: #D4AF37`) to implement pure glassmorphism.
* **Vanilla JavaScript (ES6)**: Used for handling complex asynchronous timers and the native Web Audio logic.

### Future Expansion (What we will be using post-hackathon)
* **Next.js (React Framework)**: To handle Server-Side Rendering (SSR) for blazing-fast initial load times.
* **Framer Motion**: To replace GSAP for more React-native declarative component animations.
* **Vite**: For production bundling and asset optimization.

---

## 2. BACKEND & INTEGRATION (What we use & will use)

The backend replaces manual document uploads with direct database bridging and live fraud tracking.

### Currently Implemented (What we use)
* **Python (Flask)**: The `ml_backend.py` serves as the primary intelligence node to process incoming claims.
* **Web Audio API Engine**: Synthesizes real-time sound frequencies (Metallic Thuds and Siren Alerts) directly through the browser without needing MP3 files.
* **Mock Source-Truth Logic**: JavaScript algorithms acting as mock-connectors to simulate fetching precise JSON data from external government nodes based on vocal cues.
* **QRCode.js**: A local cryptographic generator building the final "Smart Insurance Certificate".

### Future Expansion (What we will be using post-hackathon)
* **Node.js / Express**: To expand the scalable REST APIs for live telemetry data.
* **Firebase / Firestore**: For secure, encrypted, and instantaneous NoSQL storage of the generated claim certificates.
* **Actual Govt APIs**: Full OAuth2 integrations with **ABHA** (Health), **Vahan / CEIR** (Vehicle & Theft), and **Aviation Edge** (Flight Delay tracking).
* **Solidity / Polygon (Blockchain)**: Committing the final generated QR code directly to a distributed ledger to make the insurance certificate 100% immutable and cross-verifiable by other companies.

---

## 3. ARTIFICIAL INTELLIGENCE & VOICE-FLOW (The Core Agent)

This is the brain of the Zero-Input Terminal, combining your custom agents with native browser technology.

### The Voiceflow Custom Agent
* **Voiceflow Runtime API**: Your custom agent (`Project ID: 69e1b38618d5b8d8b666412e`) is successfully injected securely via `bundle.mjs`. 
* **Role**: It acts as the omnipresent, highly intelligent conversational fallback. If the user clicks the widget, the Voiceflow logic takes over, guiding the user through complex insurance FAQ processing, policy tracking, and custom Dialog Management built specifically by your team.

### Native Speech Integration (The "Golden Key" Pipeline)
* **Web Speech API (`SpeechRecognition`)**: Eliminates the keyboard. It listens strictly to the user’s answers (e.g., "I had an accident in Ambala") and translates it to string data instantly.
* **Agentic NLP Engine (Predictive Fraud)**: The code actively parses the transcript. If the user states they are in "Delhi" but the system logic detects an IP in "Ambala," it automatically overrides the flow, pulses the Vault red, and flags a Multi-Regional Fraud Breach.
* **Native TTS (`window.speechSynthesis`)**: Synthesizes the deep executive AI voice that reads the Verification Cards aloud and manages the UI steps.
