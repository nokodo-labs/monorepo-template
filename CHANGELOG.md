# Changelog

## [0.1.0](https://github.com/nokodo-labs/monorepo-template/compare/v0.0.1...v0.1.0) (2025-11-01)


### ✨ New Features

* **backend:** add SQLite support for testing and dev ([3677920](https://github.com/nokodo-labs/monorepo-template/commit/3677920f122f061a4123eb506c5ad05d546c061d))
* **frontend:** add GitHub Pages deploy workflow and static preview mode ([4675ed8](https://github.com/nokodo-labs/monorepo-template/commit/4675ed8213026212e71497522942ba2538df22cf))
* **frontend:** add Vitest testing infrastructure ([77ef97c](https://github.com/nokodo-labs/monorepo-template/commit/77ef97ccc469b05b7f771843b37b24e888a19982))
* **monorepo:** enhance dev UX and landing page polish ([974b301](https://github.com/nokodo-labs/monorepo-template/commit/974b301c2f4625a4c41cd48c5e4145483d9da0ef))
* **monorepo:** scaffold full-stack FastAPI + Svelte template ([4d4e797](https://github.com/nokodo-labs/monorepo-template/commit/4d4e7977f46c9fc42ccedbec9c38bc3f795f8e99))
* **ui:** enhance landing page visuals and UX ([7f4c1e1](https://github.com/nokodo-labs/monorepo-template/commit/7f4c1e17c5880225a1b9817454d7feabfd8299a1))
* **vscode:** enhance dev env with new extensions and config ([446bdc3](https://github.com/nokodo-labs/monorepo-template/commit/446bdc3c321446ddb180a35dec0de0af53f75d95))
* **vscode:** enhance Git integration and search config ([9453acd](https://github.com/nokodo-labs/monorepo-template/commit/9453acd6141e7b91bccfc4a305e8792e577d4d1d))


### 🐛 Bug Fixes

* **ci:** use dynamic repository name for Docker tagging ([691c57a](https://github.com/nokodo-labs/monorepo-template/commit/691c57a577e9de4b179fb75fd5e5a29a121ebe8c))
* **frontend,backend:** improve test config and Tailwind setup ([4857698](https://github.com/nokodo-labs/monorepo-template/commit/48576987eda33133431fb00df8c51978a26df111))
* **frontend:** configure module resolution paths ([dfec461](https://github.com/nokodo-labs/monorepo-template/commit/dfec461c137deea348a8085754461909fbc4746c))
* **frontend:** configure relative base path for deployment ([1b6c6d6](https://github.com/nokodo-labs/monorepo-template/commit/1b6c6d68fadf476b5c067933bb04c314797d81fd))
* **frontend:** improve type safety and enable Svelte runes ([6e36c94](https://github.com/nokodo-labs/monorepo-template/commit/6e36c94d5aedd7758f025701b10f0b29e6955f0e))
* **frontend:** restore API client files and adjust gitignore ([1613907](https://github.com/nokodo-labs/monorepo-template/commit/1613907f0c7daced66ef1e198d41dd9845b6115c))
* **test:** improve Windows async compatibility ([2cff7ba](https://github.com/nokodo-labs/monorepo-template/commit/2cff7ba104eb334e5649d64f5830825df25363fa))


### 🔧 Improvements

* **backend:** rename project_name to project_slug ([b22b5d3](https://github.com/nokodo-labs/monorepo-template/commit/b22b5d34f3fce4293c7711a689c58a4eabfe66c9))
* **ci:** consolidate workflow jobs and optimize execution ([b72c0ac](https://github.com/nokodo-labs/monorepo-template/commit/b72c0acef9ad4ed4bc6c5894716bef9c8eeed281))
* **ci:** convert promotion workflow to reusable ([ba3b448](https://github.com/nokodo-labs/monorepo-template/commit/ba3b448d248586b32661f92bca3e0239641c59de))
* **ci:** generalize promotion workflow config ([8a9986a](https://github.com/nokodo-labs/monorepo-template/commit/8a9986abcf2683aef0637aa9450ed30914e34eb9))
* **ci:** rename docker workflow from deploy to publish ([7f514ee](https://github.com/nokodo-labs/monorepo-template/commit/7f514eea359d25a582ee4a709f05bba34de36b89))
* **ci:** reorganize workflow jobs and rename Docker workflow ([1647e64](https://github.com/nokodo-labs/monorepo-template/commit/1647e643b6f6cb2d0a604317e4f42c9ed5ff064f))
* **ci:** standardize Python and Node version management ([7562dd1](https://github.com/nokodo-labs/monorepo-template/commit/7562dd1bcc1d28befb81f1219446718bfa50189c))
* **deps:** separate library and API dependencies ([c33dec7](https://github.com/nokodo-labs/monorepo-template/commit/c33dec7e1111c251b04c7e6fb57ca08f6dfd0c49))
* **frontend:** update import path and workflow name ([a6a76c1](https://github.com/nokodo-labs/monorepo-template/commit/a6a76c18cd311b828624ee95fd41980b813e0c40))
* **frontend:** use SvelteKit alias for API import ([3c4c740](https://github.com/nokodo-labs/monorepo-template/commit/3c4c74050ac55892152016a33485129f9323e0bd))
* **release:** standardize PR title patterns and labels ([372747e](https://github.com/nokodo-labs/monorepo-template/commit/372747ea03332b7c0438b95eb8041b7af731a7fd))
* standardize code formatting to tabs ([bc75c2e](https://github.com/nokodo-labs/monorepo-template/commit/bc75c2ebb533ec3be49d4fc3408891fb23cfae73))
* **template:** rename project_name to project_slug ([ecc9114](https://github.com/nokodo-labs/monorepo-template/commit/ecc9114d092e277f8ea1795b4f5dfb2a051bcd90))


### 🧹 Miscellaneous

* **alembic:** reorder imports to follow conventions ([c6b64ac](https://github.com/nokodo-labs/monorepo-template/commit/c6b64ac5c5db891d8e6b24f68eb792eca194317a))
* **deps-dev:** bump @sveltejs/vite-plugin-svelte from 5.1.1 to 6.2.1 in /frontend ([1e0d234](https://github.com/nokodo-labs/monorepo-template/commit/1e0d23419957d69a47769922cc501fe27cc80b85))
* **deps-dev:** bump @sveltejs/vite-plugin-svelte in /frontend ([b57eae4](https://github.com/nokodo-labs/monorepo-template/commit/b57eae4ec81a3699e55076f3e9aa9d94d0ce2d55))
* **deps-dev:** bump @types/node from 22.18.12 to 24.9.1 in /frontend ([eab74bc](https://github.com/nokodo-labs/monorepo-template/commit/eab74bc10102f958fbaf1a9138c554acb22c56e9))
* **deps-dev:** bump @types/node from 22.18.12 to 24.9.1 in /frontend ([3b51d8c](https://github.com/nokodo-labs/monorepo-template/commit/3b51d8c1b5e2e506d45b0ed0dfad1819367e12f4))
* **deps-dev:** bump @types/node from 24.9.1 to 24.9.2 in /frontend ([6421162](https://github.com/nokodo-labs/monorepo-template/commit/6421162efad24645e6f2495c501687ca1955ec3d))
* **deps-dev:** bump @types/node from 24.9.1 to 24.9.2 in /frontend ([da6d295](https://github.com/nokodo-labs/monorepo-template/commit/da6d295eb926608aef6473751138046569f58c80))
* **deps-dev:** bump eslint-config-prettier from 9.1.2 to 10.1.8 in /frontend ([fbf9bcc](https://github.com/nokodo-labs/monorepo-template/commit/fbf9bcc5e7d5ce320fd041d09342bf164d569d91))
* **deps-dev:** bump eslint-config-prettier in /frontend ([4e95869](https://github.com/nokodo-labs/monorepo-template/commit/4e95869a6a3c05bde04526950c554dc2a1d520d1))
* **deps-dev:** bump eslint-plugin-svelte from 2.46.1 to 3.12.5 in /frontend ([cb18099](https://github.com/nokodo-labs/monorepo-template/commit/cb18099fec4d92e519b459ef6423ddde480cdaa1))
* **deps-dev:** bump eslint-plugin-svelte in /frontend ([f9a6d44](https://github.com/nokodo-labs/monorepo-template/commit/f9a6d44530c1a7fb70c5ea19f819e7e9a8e35e1e))
* **deps-dev:** bump prettier-plugin-tailwindcss from 0.6.14 to 0.7.1 in /frontend ([5f13032](https://github.com/nokodo-labs/monorepo-template/commit/5f130322b8d8832d3bc9052ed45f0aca5db7dfe6))
* **deps-dev:** bump prettier-plugin-tailwindcss in /frontend ([e9db3ba](https://github.com/nokodo-labs/monorepo-template/commit/e9db3ba67866377627d63375fa2981ab90596243))
* **deps-dev:** bump svelte from 5.42.3 to 5.43.0 in /frontend ([9cf9867](https://github.com/nokodo-labs/monorepo-template/commit/9cf98677b42c04b6fe3b4e5142a21e55c22276d6))
* **deps-dev:** bump svelte from 5.42.3 to 5.43.0 in /frontend ([66f2b01](https://github.com/nokodo-labs/monorepo-template/commit/66f2b01bcf0a66c268305b95331db2618ae7378c))
* **deps-dev:** bump tailwindcss from 3.4.18 to 4.1.16 in /frontend ([4b5c96d](https://github.com/nokodo-labs/monorepo-template/commit/4b5c96de2ecbf869cbce8f14cf9de80f0e6915c9))
* **deps-dev:** bump tailwindcss from 3.4.18 to 4.1.16 in /frontend ([e153020](https://github.com/nokodo-labs/monorepo-template/commit/e15302092cba819dc070ca09db2ea9400f831640))
* **deps-dev:** bump vite from 6.4.1 to 7.1.12 in /frontend ([4c9215f](https://github.com/nokodo-labs/monorepo-template/commit/4c9215fa2f25042b28129d1603eee5962b6fd72d))
* **deps-dev:** bump vite from 6.4.1 to 7.1.12 in /frontend ([063c0e2](https://github.com/nokodo-labs/monorepo-template/commit/063c0e29be5cd67ed3e61a2385169f59ee5c5b7b))
* **deps:** bump actions/checkout from 4 to 5 ([e704285](https://github.com/nokodo-labs/monorepo-template/commit/e7042850ca125fe573797163a796ad0925ff8e2a))
* **deps:** bump actions/checkout from 4 to 5 ([b0eb7bf](https://github.com/nokodo-labs/monorepo-template/commit/b0eb7bfc84fa9d689f33dfdd53abaccb5d5af5da))
* **deps:** bump actions/github-script from 7 to 8 ([1772ea4](https://github.com/nokodo-labs/monorepo-template/commit/1772ea43a40b5967401491e7652441f875a4e93d))
* **deps:** bump actions/github-script from 7 to 8 ([6cf93e4](https://github.com/nokodo-labs/monorepo-template/commit/6cf93e4c1b743807e5f6f0939973adecac34c031))
* **deps:** bump actions/github-script from 7 to 8 ([1e834f3](https://github.com/nokodo-labs/monorepo-template/commit/1e834f39d47d4c0546fb88cb2f4c6c8442c663f4))
* **deps:** bump actions/github-script from 7 to 8 ([086d7fd](https://github.com/nokodo-labs/monorepo-template/commit/086d7fdad4e65b68572fa1cf59b9a31b6eb5acc9))
* **deps:** bump actions/setup-node from 4 to 6 ([5e8f7f1](https://github.com/nokodo-labs/monorepo-template/commit/5e8f7f15421bdf59ec43e09a0ab184c29b95960c))
* **deps:** bump actions/setup-node from 4 to 6 ([fc9128c](https://github.com/nokodo-labs/monorepo-template/commit/fc9128c6e72b53e605b0d9d93891b0b397c72ab9))
* **deps:** bump actions/setup-python from 5 to 6 ([cb68c28](https://github.com/nokodo-labs/monorepo-template/commit/cb68c28b1e7e2be7901b3021893c14cc1cbc4f80))
* **deps:** bump actions/setup-python from 5 to 6 ([9a76853](https://github.com/nokodo-labs/monorepo-template/commit/9a7685389a2a751242bce7f658d0ea6001723d9a))
* **deps:** bump actions/stale from 9 to 10 ([514ae6c](https://github.com/nokodo-labs/monorepo-template/commit/514ae6c71ade35ffe7ec328984812b60159ee887))
* **deps:** bump actions/stale from 9 to 10 ([cad3256](https://github.com/nokodo-labs/monorepo-template/commit/cad32563b898d2aeb142f95e3837ee1eca3d74f5))
* **deps:** bump actions/upload-pages-artifact from 3 to 4 ([2a9eb14](https://github.com/nokodo-labs/monorepo-template/commit/2a9eb14595e0630bc363ac403279e268db32106e))
* **deps:** bump actions/upload-pages-artifact from 3 to 4 ([0b9831c](https://github.com/nokodo-labs/monorepo-template/commit/0b9831cbfd525d7bc0824c17c37182467513d7b1))
* **deps:** upgrade testing dependencies to latest versions ([d81b71e](https://github.com/nokodo-labs/monorepo-template/commit/d81b71e0d1e15c95fd119b77f48add9dc67d58f8))
* **devops:** add CI/CD, release, and template customization ([d54210b](https://github.com/nokodo-labs/monorepo-template/commit/d54210b95aec48a45b02f3e6f32c9fbcbbfd8d8d))
* **frontend:** add package-lock for dependency tracking ([dffb6fa](https://github.com/nokodo-labs/monorepo-template/commit/dffb6fae15141dba3d70c2ef64b340bd52f005df))
* **frontend:** add testing infrastructure with Vitest ([c685871](https://github.com/nokodo-labs/monorepo-template/commit/c685871e5af82646878fbdcb822eac4a15f3c08b))
* **frontend:** improve CI and add path aliases ([b6147e7](https://github.com/nokodo-labs/monorepo-template/commit/b6147e7e9d8e30534730e2d5646cd03c5061e013))
* **github:** add issue templates and update docs ([f783e96](https://github.com/nokodo-labs/monorepo-template/commit/f783e960c40ed7b3439c87f48f4f6a568d2f283e))
* **users:** convert indentation from spaces to tabs ([530ee5a](https://github.com/nokodo-labs/monorepo-template/commit/530ee5a1641eba9ccf4046d5935e6f057b9dd9be))


### ♻️ Ops

* **docker:** use repository name for image tag ([1755aea](https://github.com/nokodo-labs/monorepo-template/commit/1755aea72f73c46033438d2a3a9458f0babdb88b))
* migrate to pytest and fix build contexts ([8731f95](https://github.com/nokodo-labs/monorepo-template/commit/8731f9547d7d3815b855e1b3a32ab8146e8f65b9))
* remove production branch and refine workflow triggers ([a20733b](https://github.com/nokodo-labs/monorepo-template/commit/a20733b0771c8d610723c5a6b8a45e3f0f6e743c))
* **workflows:** refine deployment and CI triggers ([1053d98](https://github.com/nokodo-labs/monorepo-template/commit/1053d98820c5d37b083ccab9fffe1e71aa9da270))


### 📚 Documentation

* **instructions:** clarify and expand usage guidelines ([b5501d9](https://github.com/nokodo-labs/monorepo-template/commit/b5501d929a023fe830def832fd461e8dd2f9fb70))
* **readme,setup:** clarify template usage and deployment ([ff6ffb1](https://github.com/nokodo-labs/monorepo-template/commit/ff6ffb18ecac660496f334496fe3408e127d2b73))
* **readme:** enhance documentation with branding and UX ([aa9cf62](https://github.com/nokodo-labs/monorepo-template/commit/aa9cf62f355af6b39258c7d9c710beaa7b2f1ca7))
* **setup:** streamline and centralize setup instructions ([ffbe3bf](https://github.com/nokodo-labs/monorepo-template/commit/ffbe3bfce7ac76687ae5fa611ec1006ef3685b9f))
* update configuration for project restructure ([baea703](https://github.com/nokodo-labs/monorepo-template/commit/baea703b18554e83be5b81f775fe41f83f0ef995))
* update README and reorganize alembic structure ([726ba2a](https://github.com/nokodo-labs/monorepo-template/commit/726ba2abd029901d27cb31d895df0792006b4275))
