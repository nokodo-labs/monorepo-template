<script lang="ts">
    import { api } from './lib/api/index'

    let health = $state<{ status: string } | null>(null)
    let mounted = $state(false)

    $effect(() => {
        mounted = true
        api.healthCheck()
            .then((data) => (health = data))
            .catch((error) => console.error('backend not ready:', error))
    })
</script>

<svelte:head>
    <style>
        @keyframes float {
            0%,
            100% {
                transform: translateY(0px) rotate(0deg);
            }
            50% {
                transform: translateY(-20px) rotate(3deg);
            }
        }
        @keyframes pulse-glow {
            0%,
            100% {
                opacity: 0.3;
            }
            50% {
                opacity: 0.6;
            }
        }
        .float-shape {
            animation: float 12s ease-in-out infinite;
        }
    </style>
</svelte:head>

<main class="relative min-h-screen overflow-hidden bg-black text-white">
    <!-- Floating background shapes -->
    <div class="pointer-events-none fixed inset-0 opacity-30">
        <div
            class="float-shape absolute top-[20%] left-[10%] h-64 w-64 rounded-full bg-zinc-800/40 blur-3xl"
            style="animation-delay: 0s;"
        ></div>
        <div
            class="float-shape absolute top-[40%] right-[15%] h-96 w-96 rounded-full bg-zinc-700/30 blur-3xl"
            style="animation-delay: 2s;"
        ></div>
        <div
            class="float-shape absolute bottom-[20%] left-[20%] h-80 w-80 rounded-full bg-zinc-800/40 blur-3xl"
            style="animation-delay: 4s;"
        ></div>
    </div>

    <!-- Content -->
    <div class="relative z-10">
        <!-- Header -->
        <header class="border-b border-zinc-800/50 backdrop-blur-sm">
            <div class="container mx-auto flex items-center justify-between px-6 py-4">
                <div class="flex items-center gap-4">
                    <img
                        src="https://nokodo.net/media/images/logo_full.svg"
                        alt="nokodo"
                        class="h-6"
                    />
                </div>
                <div class="flex items-center gap-2">
                    {#if health}
                        <div
                            class="flex items-center gap-2 rounded-full bg-green-500/10 px-3 py-1.5 text-sm font-medium text-green-400 ring-1 ring-green-500/20"
                        >
                            <div class="h-2 w-2 animate-pulse rounded-full bg-green-500"></div>
                            <span class="lowercase">online</span>
                        </div>
                    {:else}
                        <div
                            class="flex items-center gap-2 rounded-full bg-zinc-800/50 px-3 py-1.5 text-sm font-medium text-zinc-400 ring-1 ring-zinc-700/50"
                        >
                            <div
                                class="h-2 w-2 rounded-full bg-zinc-500"
                                style="animation: pulse-glow 2s ease-in-out infinite;"
                            ></div>
                            <span class="lowercase">starting...</span>
                        </div>
                    {/if}
                </div>
            </div>
        </header>

        <!-- Hero -->
        <section
            class="container mx-auto flex flex-col items-center justify-center px-6 py-24 text-center"
        >
            <div
                class="mb-10 inline-flex items-center gap-2 rounded-full bg-zinc-900/80 px-4 py-2 text-sm font-medium text-zinc-300 ring-1 ring-zinc-800"
            >
                <span class="text-lg">🚀</span>
                <span class="lowercase">production-ready monorepo</span>
            </div>

            <h1 class="mb-6 max-w-4xl text-6xl leading-tight font-bold tracking-tight md:text-7xl">
                build <span
                    class="bg-linear-to-r from-white via-zinc-200 to-zinc-400 bg-clip-text text-transparent"
                    >full-stack apps</span
                > fast
            </h1>

            <p class="mb-16 max-w-2xl text-lg text-zinc-400 lowercase">
                FastAPI + Svelte 5 + TypeScript + PostgreSQL + Docker.<br />
                type-safe API client. async-first. ready to scale.
            </p>

            <!-- Quick Start -->
            <div
                class="w-full max-w-4xl rounded-2xl bg-zinc-900/50 p-8 ring-1 ring-zinc-800 backdrop-blur-sm"
            >
                <h2 class="mb-8 text-2xl font-semibold lowercase">quick start</h2>

                <div class="space-y-6">
                    <div>
                        <div
                            class="mb-3 flex items-center gap-3 text-sm font-medium text-zinc-400 lowercase"
                        >
                            <span
                                class="flex h-8 w-8 items-center justify-center rounded-lg bg-zinc-800 text-sm font-bold text-white ring-1 ring-zinc-700"
                                >1</span
                            >
                            clone & setup
                        </div>
                        <div
                            class="ml-11 overflow-x-auto rounded-lg bg-black p-4 font-mono text-sm text-zinc-300 ring-1 ring-zinc-800"
                        >
                            <div>
                                git clone https://github.com/nokodo-labs/monorepo-template.git
                            </div>
                            <div class="mt-1">
                                cd monorepo-template/.docker && docker compose up -d
                            </div>
                        </div>
                    </div>

                    <div>
                        <div
                            class="mb-3 flex items-center gap-3 text-sm font-medium text-zinc-400 lowercase"
                        >
                            <span
                                class="flex h-8 w-8 items-center justify-center rounded-lg bg-zinc-800 text-sm font-bold text-white ring-1 ring-zinc-700"
                                >2</span
                            >
                            install dependencies
                        </div>
                        <div
                            class="ml-11 overflow-x-auto rounded-lg bg-black p-4 font-mono text-sm text-zinc-300 ring-1 ring-zinc-800"
                        >
                            <div>cd ../backend && pip install -e .[dev]</div>
                            <div class="mt-1">cd ../frontend && npm install</div>
                        </div>
                    </div>

                    <div>
                        <div
                            class="mb-3 flex items-center gap-3 text-sm font-medium text-zinc-400 lowercase"
                        >
                            <span
                                class="flex h-8 w-8 items-center justify-center rounded-lg bg-zinc-800 text-sm font-bold text-white ring-1 ring-zinc-700"
                                >3</span
                            >
                            start development
                        </div>
                        <div
                            class="ml-11 overflow-x-auto rounded-lg bg-black p-4 font-mono text-sm text-zinc-300 ring-1 ring-zinc-800"
                        >
                            <div>backend: uvicorn api.main:app --reload</div>
                            <div class="mt-1">frontend: npm run dev</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Features -->
            <div class="mt-20 grid w-full max-w-5xl gap-6 md:grid-cols-3">
                <div
                    class="rounded-xl bg-zinc-900/40 p-6 ring-1 ring-zinc-800 backdrop-blur-sm transition-all hover:bg-zinc-900/60 hover:ring-zinc-700"
                >
                    <div class="mb-4 text-3xl">⚡</div>
                    <h3 class="mb-2 text-lg font-semibold lowercase">type safety</h3>
                    <p class="text-sm text-zinc-400 lowercase">
                        OpenAPI-generated TypeScript types. compile-time API validation.
                    </p>
                </div>

                <div
                    class="rounded-xl bg-zinc-900/40 p-6 ring-1 ring-zinc-800 backdrop-blur-sm transition-all hover:bg-zinc-900/60 hover:ring-zinc-700"
                >
                    <div class="mb-4 text-3xl">🧪</div>
                    <h3 class="mb-2 text-lg font-semibold lowercase">fully tested</h3>
                    <p class="text-sm text-zinc-400 lowercase">
                        pytest + async fixtures. API, SDK, and E2E test structure ready.
                    </p>
                </div>

                <div
                    class="rounded-xl bg-zinc-900/40 p-6 ring-1 ring-zinc-800 backdrop-blur-sm transition-all hover:bg-zinc-900/60 hover:ring-zinc-700"
                >
                    <div class="mb-4 text-3xl">🐳</div>
                    <h3 class="mb-2 text-lg font-semibold lowercase">Docker ready</h3>
                    <p class="text-sm text-zinc-400 lowercase">
                        PostgreSQL 17, Nginx, dev/prod profiles. one command to start.
                    </p>
                </div>
            </div>
        </section>

        <!-- Footer -->
        <footer class="border-t border-zinc-800/50 backdrop-blur-sm">
            <div class="container mx-auto px-6 py-8 text-center text-sm text-zinc-500 lowercase">
                <p>
                    built by <a
                        href="https://nokodo.net"
                        class="font-medium text-zinc-300 transition-colors hover:text-white"
                        >nokodo labs</a
                    >
                    •
                    <a
                        href="https://nokodo.net/github"
                        class="font-medium text-zinc-300 transition-colors hover:text-white"
                        >github</a
                    >
                    • licensed under
                    <a
                        href="https://github.com/nokodo-labs/monorepo-template/blob/main/LICENSE"
                        class="font-medium text-zinc-300 transition-colors hover:text-white"
                        >BSD 3-clause</a
                    >
                </p>
            </div>
        </footer>
    </div>
</main>
