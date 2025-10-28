<script lang="ts">
    import Counter from './lib/Counter.svelte'
    import { api } from './lib/api/index'

    let health = $state<{ status: string } | null>(null)
    let loading = $state(false)

    async function checkHealth() {
        loading = true
        try {
            health = await api.healthCheck()
        } catch (error) {
            console.error('Failed to check health:', error)
        } finally {
            loading = false
        }
    }
</script>

<main class="min-h-screen bg-gradient-to-br from-purple-500 to-pink-500 p-8">
    <div class="mx-auto max-w-4xl">
        <div class="rounded-lg bg-white p-8 shadow-2xl dark:bg-gray-800">
            <h1 class="mb-4 text-4xl font-bold text-gray-900 dark:text-white">Monorepo Template</h1>

            <p class="mb-6 text-gray-600 dark:text-gray-300">
                FastAPI + Svelte 5 + TailwindCSS + Docker
            </p>

            <div class="mb-8">
                <Counter />
            </div>

            <div class="rounded-lg border border-gray-200 p-4 dark:border-gray-700">
                <h2 class="mb-3 text-xl font-semibold text-gray-900 dark:text-white">
                    Backend Health Check
                </h2>

                <button
                    onclick={checkHealth}
                    disabled={loading}
                    class="rounded bg-blue-500 px-4 py-2 font-bold text-white hover:bg-blue-700 disabled:opacity-50"
                >
                    {loading ? 'Checking...' : 'Check Backend Health'}
                </button>

                {#if health}
                    <div
                        class="mt-4 rounded bg-green-100 p-3 text-green-800 dark:bg-green-900 dark:text-green-200"
                    >
                        Backend Status: {health.status}
                    </div>
                {/if}
            </div>
        </div>
    </div>
</main>
