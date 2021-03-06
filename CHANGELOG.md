# [2.30.0](https://github.com/stencila/hub/compare/v2.29.2...v2.30.0) (2020-06-02)


### Bug Fixes

* **deps:** update dependency @stencila/encoda to v0.94.0 ([7d579d1](https://github.com/stencila/hub/commit/7d579d14b39cdb019285762635ba0b995928450a))
* **deps:** update dependency django-allauth to v0.42.0 ([ecf6258](https://github.com/stencila/hub/commit/ecf6258ebb19606a74468a8dda55e2c3c245ffea))
* **deps:** update dependency google-api-python-client to v1.8.4 ([fa26cfe](https://github.com/stencila/hub/commit/fa26cfecf155334e7272c4056a30684dea71034e))
* **deps:** update dependency httpx to v0.13.3 ([6dc9b42](https://github.com/stencila/hub/commit/6dc9b42ea09c23013321c92e87232be9ad7ffef6))
* **deps:** update dependency prometheus_client to v0.8.0 ([5815f29](https://github.com/stencila/hub/commit/5815f29965695ac8d38abd31b282992b6b03c23d))
* **Director:** Link new oauth user by verified email ([2012200](https://github.com/stencila/hub/commit/20122006b1a668af1d1a6b44a204e1bc0344ffe0))
* **Director:** Prefer primary email when matching ([3cd6d34](https://github.com/stencila/hub/commit/3cd6d348c65a2e31b17bfae53e406bd8fc1b439c))
* **Director:** Remember last login provider ([f092c2e](https://github.com/stencila/hub/commit/f092c2e36a8eb82e466c9dec5399de4da3883459))
* **Director:** Save emails from new social account ([a255ea1](https://github.com/stencila/hub/commit/a255ea1ebd1f3b6876902de912d53f0273565215))
* **Director:** Use verified github emails in match ([839d726](https://github.com/stencila/hub/commit/839d726f362bc054adbf96ba4f895563e476a0bb))


### Features

* **Overseer:** Add metrics for jobs and workers per queue ([ac48429](https://github.com/stencila/hub/commit/ac484295c4dd2c9b3e645d0f1b48655df7330c69))

## [2.29.2](https://github.com/stencila/hub/compare/v2.29.1...v2.29.2) (2020-05-26)


### Bug Fixes

* **Worker:** Do not ignore util ([249b7a8](https://github.com/stencila/hub/commit/249b7a8795ebc36d1785a3afbe4bb59f2b9904b4))

## [2.29.1](https://github.com/stencila/hub/compare/v2.29.0...v2.29.1) (2020-05-26)


### Bug Fixes

* **Broker:** Add volume for presistence across restarts ([1a4411a](https://github.com/stencila/hub/commit/1a4411aba4393d4e78182b5a40eaf2cebc5b028c))
* **deps:** update dependency google-api-python-client to v1.8.3 ([551ee4f](https://github.com/stencila/hub/commit/551ee4f9e882dd21899f2a61b0be5748d0c9c1ce))
* **Director:** Add plos source ([fb72b45](https://github.com/stencila/hub/commit/fb72b452be31bf9f213c7de17e2bc10627dcebfe))
* **Director:** Do not force rediret internal API endpoints ([914ba90](https://github.com/stencila/hub/commit/914ba9046dc193d1f34f01956e3d107dd1ed6416))
* **Director:** Trigger gdoc pull job from source ([1efa569](https://github.com/stencila/hub/commit/1efa569226a00b9373ec4f1951333b2d8f4feaa4))
* **Director:** Trigger github pull job from source ([f4c7c8c](https://github.com/stencila/hub/commit/f4c7c8c1a52e5f5c479604b848eb318c0741cc21))
* **Director:** Trigger pull job from GDrive source ([7f37a52](https://github.com/stencila/hub/commit/7f37a52e36122d33c03917a3f23c8da311b3a8bf))
* **Worker:** Google docs pull job ([692ec41](https://github.com/stencila/hub/commit/692ec4163ee48c0927cf34a4a159046f082d206f))
* **Worker:** Pull from github sources ([423c3aa](https://github.com/stencila/hub/commit/423c3aa2f0c8ca6ec83526d1a63254a4b3517d2d))
* **Worker:** Pull into a subdirectory ([cfb2d75](https://github.com/stencila/hub/commit/cfb2d753a2de816f077771812ca9a54a511a370e))
* **Worker:** Pull job for Google Drive folder ([e97efac](https://github.com/stencila/hub/commit/e97efacea885fa6fb8690729107a2bc2a88b8994))
* **Worker:** Pull single file from github ([78b8361](https://github.com/stencila/hub/commit/78b83616927383aba7c75511bf61c574e85dc227))
* **Worker:** Push job for google doc ([06511d7](https://github.com/stencila/hub/commit/06511d7f559fefa43fd528a56464313455052c1d))

# [2.29.0](https://github.com/stencila/hub/compare/v2.28.0...v2.29.0) (2020-05-26)


### Bug Fixes

* **API exception handler:** Handle non-dict exception data ([c7ff9d9](https://github.com/stencila/hub/commit/c7ff9d92f85dcd5aa990430ebd3a6dd0414d9403))
* **Director:** Project serializer to handle both create and update ([a997547](https://github.com/stencila/hub/commit/a9975479d2f9d416f0090298e183eac6d325b86b))
* **Director:** Use form helpers for jobs cancel ([f4336c9](https://github.com/stencila/hub/commit/f4336c926a512376ca7b0ff768fba7c63da90d0d))


### Features

* **Director:** Add section to delete project to settings ([6867f9e](https://github.com/stencila/hub/commit/6867f9e6d549c3fdd6945359fb903a63df84dce6)), closes [#402](https://github.com/stencila/hub/issues/402)
* **Director:** Better handling of errors and success URL ([1d5c5e1](https://github.com/stencila/hub/commit/1d5c5e1769f02e16f1a6dc155b0d6f32466c7d39))
* **Director API:** Add destroy action for projects ([596f4d6](https://github.com/stencila/hub/commit/596f4d600b63e3791ace52b2c65c9f6789e5eed9))

# [2.28.0](https://github.com/stencila/hub/compare/v2.27.2...v2.28.0) (2020-05-24)


### Bug Fixes

* **jobs:** update to css modifiers ([3da5682](https://github.com/stencila/hub/commit/3da56828aba366bdcc0c5ded2247d4fd614b2a4a))
* **projects:** adjusted padding on form as per [#434](https://github.com/stencila/hub/issues/434) ([741e47e](https://github.com/stencila/hub/commit/741e47e4888f09493414812a143d590fe9a5fe17))


### Features

* **Director:** UI updates to jobs listing ([6742d85](https://github.com/stencila/hub/commit/6742d8584d64cc12ccff68cc395e32ff603b07b9))
* **Director:** updating job filters ([b879d92](https://github.com/stencila/hub/commit/b879d928084bb799ab636d29415461aab9fb3b83))
* **job:** updates to job filtering [#453](https://github.com/stencila/hub/issues/453) ([fb0728d](https://github.com/stencila/hub/commit/fb0728d8df83afdfdbe34746be38e98e1561a841))
* **jobs:** job cancel action added. ([be50f4c](https://github.com/stencila/hub/commit/be50f4cf4f1f27710a3609f7f63ff56fc733f433))

## [2.27.2](https://github.com/stencila/hub/compare/v2.27.1...v2.27.2) (2020-05-24)


### Bug Fixes

* **deps:** update dependency @stencila/encoda to v0.93.11 ([79b650e](https://github.com/stencila/hub/commit/79b650ed049644ed6d57d2f025c33b9087362798))
* **deps:** update dependency @stencila/thema to v2.10.1 ([5ccce01](https://github.com/stencila/hub/commit/5ccce0121db93ded7bd8be463d454cebda72e566))
* **deps:** update dependency httpx to v0.13.1 ([ec63eca](https://github.com/stencila/hub/commit/ec63eca5a109c72334feb13f8efb07f1005af72a))
* **deps:** update dependency lxml to v4.5.1 ([28eeefa](https://github.com/stencila/hub/commit/28eeefa8d423354c188632ad930c86864b54cc67))
* **deps:** update dependency stencila-schema to v0.43.1 ([0fe218f](https://github.com/stencila/hub/commit/0fe218ff6648dee1e79ca0c152734226c278497c))

## [2.27.1](https://github.com/stencila/hub/compare/v2.27.0...v2.27.1) (2020-05-19)


### Bug Fixes

* **Director:** Fix API for cancelling a job [skip ci] ([43a6920](https://github.com/stencila/hub/commit/43a69204819c442d87d7b4666d42a2a6f5c17d4e))
* **Director:** Fix API job retrieve view [skip ci] ([393310c](https://github.com/stencila/hub/commit/393310c38313934d5c143df4254eb6e437687645))
* **Director:** Jobs API: use permissions guard ([a6034dd](https://github.com/stencila/hub/commit/a6034ddae84204ede43d62c50a173b889b3ee1c4))

# [2.27.0](https://github.com/stencila/hub/compare/v2.26.0...v2.27.0) (2020-05-19)


### Bug Fixes

* **Director:** merge conflict errors ([decad48](https://github.com/stencila/hub/commit/decad482f2b3ed292ac5e9b84eddd2b873476fea))
* **jobs:** lint error ([adcc625](https://github.com/stencila/hub/commit/adcc6251dafaf1b17536913fbb5d5f286c51da82))
* **jobs:** Updates to PR [#448](https://github.com/stencila/hub/issues/448) ([ded1cdf](https://github.com/stencila/hub/commit/ded1cdf858e229c2439a0d2c3f9fcc962cf9904c))


### Features

* **Director:** added jobs details template/view ([1f39400](https://github.com/stencila/hub/commit/1f394009646f4db9c4778e25a43f848f6c656a27))
* **Director:** added jobs to main dropdown nav ([1e73ec1](https://github.com/stencila/hub/commit/1e73ec192634e39e143df884fa7f475f3666bec9))
* **Director:** adding jobs view ([52c4abf](https://github.com/stencila/hub/commit/52c4abf8cbd0f3ff12bd2324fa4283f2f433cab6))
* **Director:** completion of jobs list template ([43e3ad7](https://github.com/stencila/hub/commit/43e3ad749b12b8302ee4fe74baa06f0c6bb34765))
* **Director:** removing jobs script for now ([b54164c](https://github.com/stencila/hub/commit/b54164cb3856a58565af6eaf7138c15a0eb15033))
* **Director:** removing jobs script for now ([e583825](https://github.com/stencila/hub/commit/e583825f1cd0cb657ba12d69a40c70cd55301ac5))
* **Director:** rollback of unecessary Docker/npm changes ([4880a61](https://github.com/stencila/hub/commit/4880a6127fc2953b1bc6a4da2f03dc00484706d6))
* **Director:** Setting up jobs urls and views ([e3f90b5](https://github.com/stencila/hub/commit/e3f90b58807e65afcb2ca38a32adda936f38949f))
* **Director:** wip - adding job creation script ([6888b11](https://github.com/stencila/hub/commit/6888b11bfcf1ed58d562d4d5e69e7253d83e58d3))
* **jobs:** wiring up templates to test data ([87c5bdf](https://github.com/stencila/hub/commit/87c5bdf1617bf0ee3a19132e90756ff8aae82b83))

# [2.26.0](https://github.com/stencila/hub/compare/v2.25.2...v2.26.0) (2020-05-17)


### Bug Fixes

* **Director:** Add request_permissions_guard ([e93b417](https://github.com/stencila/hub/commit/e93b417e8eb84d4d656ece7ba5baaa32a7bccec3)), closes [#398](https://github.com/stencila/hub/issues/398)


### Features

* **Director:** Create pull job for sources ([44533ef](https://github.com/stencila/hub/commit/44533efa7f2151b00f4af632933a289e4f90d9a5))
* **Director:** Update job model and API views ([9ba9ac3](https://github.com/stencila/hub/commit/9ba9ac350e5211d5d9005b59268af0698dc82ed9))

## [2.25.2](https://github.com/stencila/hub/compare/v2.25.1...v2.25.2) (2020-05-16)


### Bug Fixes

* **CI:** Remove copy of top package.json ([62d2c32](https://github.com/stencila/hub/commit/62d2c325738bfbceeda242d36b481a505a581126))

## [2.25.1](https://github.com/stencila/hub/compare/v2.25.0...v2.25.1) (2020-05-16)


### Bug Fixes

* **Director:** Change location of Encoda install ([a9277ae](https://github.com/stencila/hub/commit/a9277aed134de12e7a33fcdeffa957d0ceb760d6))

# [2.25.0](https://github.com/stencila/hub/compare/v2.24.1...v2.25.0) (2020-05-15)


### Bug Fixes

* **deps:** update dependency @stencila/thema to v2.7.3 ([2d98e00](https://github.com/stencila/hub/commit/2d98e00ccd42f3634ea5340a3965684b55d65fcb))


### Features

* **CSS:** Colocate Styles package inside Hub ([2f03bb7](https://github.com/stencila/hub/commit/2f03bb7b8822cc2e18e8ae5bc128c0c8578148ec))

## [2.24.1](https://github.com/stencila/hub/compare/v2.24.0...v2.24.1) (2020-05-14)


### Bug Fixes

* **Worker:** plos pull job ([75e682e](https://github.com/stencila/hub/commit/75e682e4d2dbc374ee3d3d0a6179593b4264c617))

# [2.24.0](https://github.com/stencila/hub/compare/v2.23.1...v2.24.0) (2020-05-14)


### Bug Fixes

* **Worker:** Add malicious host test from director ([6a0cd66](https://github.com/stencila/hub/commit/6a0cd669ccc3f6e107fd743d06adc60b7fd1f5e9))
* **Worker:** Decode returned bytes from subprocess ([7be8161](https://github.com/stencila/hub/commit/7be8161160ca8fb7a540c9d4c94b339b4409e793))
* **Worker:** Fix handling on bytes input ([8fa59db](https://github.com/stencila/hub/commit/8fa59dbb283f0f4ba434574fd535c8fbf6edc334))
* **Worker:** Use requests.session for elife pull ([075f7a3](https://github.com/stencila/hub/commit/075f7a3c82ec6d20c4840aa41e2f443c1638867c))


### Features

* **Worker:** Add a Convert job ([7fbb23e](https://github.com/stencila/hub/commit/7fbb23e0f1a30558603c87a849cc7b660d748170))
* **Worker:** Add Decode and Encode jobs ([87dba8c](https://github.com/stencila/hub/commit/87dba8c76870644d9b7603f050ad29f1f97286d0))
* **Worker:** Add SubprocessJob ([10f5536](https://github.com/stencila/hub/commit/10f553666c16be08a91043b61238789bd1bdc306))
* **Worker:** SubprocessJob can accept stdin ([88b3b80](https://github.com/stencila/hub/commit/88b3b805c662ff5ec9c9657292a2a7f4a04de339))

## [2.23.1](https://github.com/stencila/hub/compare/v2.23.0...v2.23.1) (2020-05-13)


### Bug Fixes

* **Scheduler:** Update broker url ([454db11](https://github.com/stencila/hub/commit/454db11280d6ed830d824ca07faf3853aeb09960))
* **Worker:** Fetch figures in elife pull job ([a1331c4](https://github.com/stencila/hub/commit/a1331c4c8deb975d3ca2ed6ab1bff8bb3c11cca6))
* **Worker:** Ignore W503 linting rule ([d402977](https://github.com/stencila/hub/commit/d40297734988c74860d1fd2eb6b7d71a63ba7082))

# [2.23.0](https://github.com/stencila/hub/compare/v2.22.0...v2.23.0) (2020-05-11)


### Bug Fixes

* **Overseer:** Do not handles results (incl exceptions) ([f26f464](https://github.com/stencila/hub/commit/f26f464fcfd07d1628f0c633364d0babf5c63d64))


### Features

* **Worker:** Add KubernetesSession ([60b6f2a](https://github.com/stencila/hub/commit/60b6f2a15a0fb9244a09a07b87f23695cf45042b))

# [2.22.0](https://github.com/stencila/hub/compare/v2.21.2...v2.22.0) (2020-05-09)


### Features

* **Director:** Add queue model and associated API views ([39440c3](https://github.com/stencila/hub/commit/39440c3039cd8e88b1573cc75928fa602e59317e))

## [2.21.2](https://github.com/stencila/hub/compare/v2.21.1...v2.21.2) (2020-05-07)


### Bug Fixes

* **Overseer:** Add monitoring metrics ([42bf0b2](https://github.com/stencila/hub/commit/42bf0b268562846a4b06be2c190418c720686ce9))
* **Overseer:** File super() call; rename metric ([765362b](https://github.com/stencila/hub/commit/765362bc801e7169ac7c0b3c253cccf829619ea1))

## [2.21.1](https://github.com/stencila/hub/compare/v2.21.0...v2.21.1) (2020-05-06)


### Bug Fixes

* **Director:** Do not redirect internal URLs to HTTPS ([0bef198](https://github.com/stencila/hub/commit/0bef198cd68716d2e6f07878aab627446c36a478))

# [2.21.0](https://github.com/stencila/hub/compare/v2.20.7...v2.21.0) (2020-05-05)


### Bug Fixes

* **Monitor:** Specify the retention time and size ([e6dced0](https://github.com/stencila/hub/commit/e6dced0ed7d1236a4b3be142c9f08bafe6231a00)), closes [/github.com/helm/charts/blob/5597f269685b8e3220e2a181fbf002b1b1b819e0/stable/prometheus/values.yaml#L763-L765](https://github.com//github.com/helm/charts/blob/5597f269685b8e3220e2a181fbf002b1b1b819e0/stable/prometheus/values.yaml/issues/L763-L765)
* **Monitor:** Use metric_path so that monitoring self works ([3859a99](https://github.com/stencila/hub/commit/3859a997084c142c362484323f5a1562e453f9f7))


### Features

* **Director:** Enable Prometheus metrics ([1074428](https://github.com/stencila/hub/commit/1074428375c152f3972874b7099ac77bad86d821))
* **Monitor:** Add monitor service ([e8481f7](https://github.com/stencila/hub/commit/e8481f72fae624163f1ad7674f4ca591f85b32a6))
* **Router:** Add route to monitor ([f8dc056](https://github.com/stencila/hub/commit/f8dc0561b510309713395f6c1fd84fd79533eed4))

## [2.20.7](https://github.com/stencila/hub/compare/v2.20.6...v2.20.7) (2020-05-05)


### Bug Fixes

* **Director:** Update Encoda version ([2b1e38d](https://github.com/stencila/hub/commit/2b1e38d3036e90a091d8176da84a977975546d7c))

## [2.20.5](https://github.com/stencila/hub/compare/v2.20.4...v2.20.5) (2020-05-05)


### Bug Fixes

* **CI:** Specify docker-compose file ([269575b](https://github.com/stencila/hub/commit/269575befbe8c9479a0f5e8f210c282eaf1fd204))

## [2.20.4](https://github.com/stencila/hub/compare/v2.20.3...v2.20.4) (2020-05-05)


### Bug Fixes

* **deps:** update dependency @stencila/thema to v2.7.0 ([88648c6](https://github.com/stencila/hub/commit/88648c66e8657e3ca59b63f635ca811d27e60e6d))
* **deps:** update dependency pillow to v7.1.2 ([793a667](https://github.com/stencila/hub/commit/793a66735596dcf0b42b275249e1189ddd2ed57c))
* **Deps:** Upgrade Theme version ([3e63780](https://github.com/stencila/hub/commit/3e63780139fca8620acafb9324e36b0753b5b19c))
* **Router:** Custom error page and reporting for 502 and 504 erors ([20985e6](https://github.com/stencila/hub/commit/20985e649cdcef00e88156826fb0c2aac0ee5ff2))

## [2.20.3](https://github.com/stencila/hub/compare/v2.20.2...v2.20.3) (2020-05-04)


### Bug Fixes

* **Director config:** Add config vars for Google Storage ([14af313](https://github.com/stencila/hub/commit/14af313a796deb98f9fba3d98bafcf323a51d6b7))

## [2.20.2](https://github.com/stencila/hub/compare/v2.20.1...v2.20.2) (2020-05-04)


### Bug Fixes

* **Router:** Make entrypoint.sh executable ([7029ec2](https://github.com/stencila/hub/commit/7029ec22ede787449f2c84af1e408114b72a4051))

## [2.20.1](https://github.com/stencila/hub/compare/v2.20.0...v2.20.1) (2020-05-04)


### Bug Fixes

* **Director:** Add INTERCOM_ACCESS_TOKEN setting ([1c53363](https://github.com/stencila/hub/commit/1c533631f09d9dbee5829f1f8f887d112865c9e8))

# [2.20.0](https://github.com/stencila/hub/compare/v2.19.0...v2.20.0) (2020-05-03)


### Bug Fixes

* **AccountsJobsViewSet:** Turn on permisson class ([4cf74e7](https://github.com/stencila/hub/commit/4cf74e72a0dbde6ff75ac5df5b22f7fff9ca0fa9))
* **API exception handler:** Output traceback ([90e1d4e](https://github.com/stencila/hub/commit/90e1d4ee526ab2fd09c5be736439165eac797d23))
* **API URLs:** Prefix with carat to avoid clash ([ac4b8df](https://github.com/stencila/hub/commit/ac4b8df6293402562e6b82695116909d934a9038))
* **Director Job API:** Allow for setting of fields during update ([4dd0e9f](https://github.com/stencila/hub/commit/4dd0e9fc713a67a6aca0aeaa6cc5019e6bb10f35))
* **Director settings:** No prefix on env var ([d4e1538](https://github.com/stencila/hub/commit/d4e1538e4daa6364e17c740692cc4ba0d0e5dd8b))
* **Docker compose:** Make router accessible on host ([112d139](https://github.com/stencila/hub/commit/112d139ed45c33270d5553b97066bd05242f963a))
* **Jobs:** Call save on job serializer ([83d04be](https://github.com/stencila/hub/commit/83d04bec78e935fa151e80c2e08cc019fa0bf828))
* **Jobs connect:** Allow for Websockets ([35f33fb](https://github.com/stencila/hub/commit/35f33fb9ae3b0f62c73c36de86254609e117bc25))
* **Overseer:** Allow overseer to use basic auth to connect ([33835cf](https://github.com/stencila/hub/commit/33835cf2bf3f3aa6142ac88b5deab6b803fcb791))
* **Router:** Clear authorization header ([4795620](https://github.com/stencila/hub/commit/47956208e071d1302444578be23a7ed775593d4a))
* **Router:** Disable internal route to broker ([1c88a3f](https://github.com/stencila/hub/commit/1c88a3f9edb6f5784c231aa46da5d18cb60c005f))
* **Schedular Dockerfile:** Run as non-root user ([302bb56](https://github.com/stencila/hub/commit/302bb5626bafd4a5a6734315a1d56fe4846651b7))
* **Scheduler:** Add dockerignore to avoid pid files etc polluting container during development ([fc21b5f](https://github.com/stencila/hub/commit/fc21b5f04d9f0d94dbcbf89d9437c8da63ff945e))
* **Scheduler:** Configure beat_scheduler properly; add time zone awareness setting ([3ab621b](https://github.com/stencila/hub/commit/3ab621b83628b28ed608b3083dcd0718aa1e6938))
* **Scheduler:** Point to dev db ([ddd0abd](https://github.com/stencila/hub/commit/ddd0abd6a35bdc9a550c2bd168a9a743627d52e9))
* **Scheduler:** Specify log level INFO ([959d01d](https://github.com/stencila/hub/commit/959d01d2ce0dd635850e3b0820cf359cfcfae428))
* **Users API:** Differentiate between public and private user fields ([424f401](https://github.com/stencila/hub/commit/424f401fcd9d8337d0ae0ebf1329fce3a3a06f47))
* **Worker:** Ensure all modules are copied to Docker ([9eb568f](https://github.com/stencila/hub/commit/9eb568f9d369a444fe60a9784329a06af5a91857))
* **Worker:** Use Director API instead of Database connection ([67721e8](https://github.com/stencila/hub/commit/67721e83e4068959ce346a20eaeae278219f7100))


### Features

* **Broker:** Move from Redis to RabbitMQ for broker ([8d455bd](https://github.com/stencila/hub/commit/8d455bdec1e8512f4b1deed83e59cfa885c6802c))
* **Broker role:** Add broker role ([768f2e6](https://github.com/stencila/hub/commit/768f2e69fff96c4799228fd9e16e87cc4593b01e))
* **Database role:** Add a (currently) pseudo database role ([21a88d9](https://github.com/stencila/hub/commit/21a88d9d54fb49b309b8c213f6d8d85083b1c00d))
* **Deps:** Add django-celery-beat for periodic jobs ([e2880ca](https://github.com/stencila/hub/commit/e2880ca201ed9a9cd0a818135207aef999c56a71))
* **Job sessions:** Allow for connection to a job session ([fa1e9f1](https://github.com/stencila/hub/commit/fa1e9f1969d428675ff64564c06b7c19d9eece93))
* **Job sessions:** Allow for connection to a job session ([fb7a177](https://github.com/stencila/hub/commit/fb7a177a232d276fe2651b713d1d918f52bd004a))
* **Job zones:** Add zones for jobs to be run in ([fa6b1ff](https://github.com/stencila/hub/commit/fa6b1ff1685219a40d12110e603d79c56b2ac44f))
* **Jobs:** Add models and API endpoints for jobs ([74b516d](https://github.com/stencila/hub/commit/74b516d584f9427870b0c5adf67ca5ac8a523af3))
* **Jobs:** Allow for cancellation of jobs ([383f2f5](https://github.com/stencila/hub/commit/383f2f53a788b69927f1e8f768d4c7142327936b))
* **Jobs:** Record users who have connected to each job ([b6c151e](https://github.com/stencila/hub/commit/b6c151ec5628fddd32441d665e56eabc8d15cab4))
* **Jobs API:** Add endpoint to access per-account job broker ([233d879](https://github.com/stencila/hub/commit/233d879e27750bc130d93132dca9b7122671979e))
* **Monitor:** Add a monitor service ([584c1c8](https://github.com/stencila/hub/commit/584c1c8a4e37a6e919940bbc339829de898f5146))
* **Router:** Allow passing of DIRECTOR_URL as env var ([70999db](https://github.com/stencila/hub/commit/70999db373986cf9dcf7f3d3108323d310973fb4))
* **Scheduler:** Add role for scheduling periodic jobs ([4916405](https://github.com/stencila/hub/commit/491640558136d9193d3adf8ee6994c2713ff3074))
* **Users API:** Return the accounts for a user ([2e69a30](https://github.com/stencila/hub/commit/2e69a306fc7ccc5ec038533b94ae165e5e36eeec))
* **Worker:** Add Worker role for running jobs ([5eba8bd](https://github.com/stencila/hub/commit/5eba8bdd9c853d225e91fcb73ba4e7352c5999cf))
* **Worker:** Use executa base image ([974b734](https://github.com/stencila/hub/commit/974b734bf21b003c6a0818c3918f133586cb4094))
* **Workers:** Add initial API for recording workers and their status ([1074991](https://github.com/stencila/hub/commit/1074991bdf3a5fbe366e810660565f1b58cf053d))
* **Workers API:** Add endpoint to get worker status time series ([05e699b](https://github.com/stencila/hub/commit/05e699b8531f65a0fc833d98d07c95abc0e0a8fb))

# [2.19.0](https://github.com/stencila/hub/compare/v2.18.2...v2.19.0) (2020-04-28)


### Features

* Permissions improvements for AccountPermissionsMixin. Close [#391](https://github.com/stencila/hub/issues/391) ([a621c2c](https://github.com/stencila/hub/commit/a621c2c20a6c54e06c02800bd77200cde68cdbd1))

## [2.18.2](https://github.com/stencila/hub/compare/v2.18.1...v2.18.2) (2020-04-28)


### Bug Fixes

* **deps:** update dependency @stencila/thema to v2.3.0 ([2c0dc4d](https://github.com/stencila/hub/commit/2c0dc4dcd8c3411d6d446bef2ad453b3650a181e))
* **deps:** update dependency dj-stripe to v2.3.0 ([7a8d527](https://github.com/stencila/hub/commit/7a8d527791ce59bf569437f31ef2bc3b97695676))
* **deps:** update dependency google-api-python-client to v1.8.2 ([ce92687](https://github.com/stencila/hub/commit/ce92687864d0ca4bbc222dab0acd322b6e7eb7b6))
* **deps:** update dependency stencila-schema to v0.43.0 ([d036243](https://github.com/stencila/hub/commit/d036243cb3377785af973a5aa717280e37520a7a))
* **Deps:** Update Thema version ([b915bef](https://github.com/stencila/hub/commit/b915befb2497c5f8f078eee961b341857cddf1ae))

## [2.18.1](https://github.com/stencila/hub/compare/v2.18.0...v2.18.1) (2020-04-21)


### Bug Fixes

* Catching ValidationError instead of ValueError on google docs URL parse. Fix [#387](https://github.com/stencila/hub/issues/387) ([03900ba](https://github.com/stencila/hub/commit/03900bacf3e4b814a5c173239a32d71e20a8fed7))
* Limiting Project creation to users' Accounts in API ([66c0a7f](https://github.com/stencila/hub/commit/66c0a7f2549b9ed5df21311dd4c3979e3d19c7c0))
* Removed double project get call in API ([269437c](https://github.com/stencila/hub/commit/269437cf9322a952e04d15539b67b19b22f05124))
* Removed use of base get/post/delte methods on ProjectPermissionsMixin. Fix [#380](https://github.com/stencila/hub/issues/380) ([3d064a9](https://github.com/stencila/hub/commit/3d064a976cb9058f5c06898b46c53e07ec9d417f))
* **deps:** update dependency @stencila/thema to v2.2.7 ([06bb61b](https://github.com/stencila/hub/commit/06bb61bb9dcd1e802199044a64c9047889d1b2e0))

# [2.18.0](https://github.com/stencila/hub/compare/v2.17.0...v2.18.0) (2020-04-16)


### Bug Fixes

* **API:** Exception handler return 500 on error ([0867231](https://github.com/stencila/hub/commit/0867231a630f1e30de70877d99073756d8deb118))
* **API URLs:** Apply consistent approach to routers and trailing slashes ([ecc5023](https://github.com/stencila/hub/commit/ecc50236d54192b9ea09e239afd5c979185464a9))
* **Source models:** Type name in Q must be lower case ([5012229](https://github.com/stencila/hub/commit/5012229a6c8b1afc66a708fa953172f07e68ffb1))


### Features

* **Source models:** Add creator and created fields ([e96ba77](https://github.com/stencila/hub/commit/e96ba77e9fd72a7cb838e7bc10ade01c501e9209))
* **Source models:** Add parse_address and related methods ([0065dbd](https://github.com/stencila/hub/commit/0065dbda8545a8c879ff79ed9c4bcb98b5860c9d))
* **Sources admin:** Add admins for source types ([ae0c391](https://github.com/stencila/hub/commit/ae0c391e92dfbd92381596996d02e02d5ef54ad4))

# [2.17.0](https://github.com/stencila/hub/compare/v2.16.1...v2.17.0) (2020-04-15)


### Features

* **Deps:** Upgrade Encoda and Thema and add Encoda to package.json ([9b211eb](https://github.com/stencila/hub/commit/9b211eb5c39646c2363e32603446df3971aca48b))

## [2.16.1](https://github.com/stencila/hub/compare/v2.16.0...v2.16.1) (2020-04-13)


### Bug Fixes

* **deps:** update dependency psycopg2-binary to v2.8.5 ([c76cfb8](https://github.com/stencila/hub/commit/c76cfb89d9f47f3c7fef34c2998afd0a1026955c))

# [2.16.0](https://github.com/stencila/hub/compare/v2.15.0...v2.16.0) (2020-04-10)


### Bug Fixes

* **Snapshot archive:** Use API view and remove project archiver ([107cbc1](https://github.com/stencila/hub/commit/107cbc128fcc4284bbb70b8ab847d97fa67d3442))


### Features

* **Snapshots API:** Add archive formats for retrieval ([afdccc9](https://github.com/stencila/hub/commit/afdccc91fa75eb8f6e32a6d829bf713b823d307a))

# [2.15.0](https://github.com/stencila/hub/compare/v2.14.1...v2.15.0) (2020-04-10)


### Bug Fixes

* **Snapshots UI:** Provide link to newly created snapshot ([b438640](https://github.com/stencila/hub/commit/b438640fe89becceefaf65ef5be9326e4b391a62))
* **Status API:** Remove pagination ([5618192](https://github.com/stencila/hub/commit/5618192dfee21b7248b8964b0565c400f4cc12b9))


### Features

* **User API:** Add list and "me" user endpoints ([b413702](https://github.com/stencila/hub/commit/b413702ba0769305e8cb7f3eaf37f85cf03c8c88))

## [2.14.1](https://github.com/stencila/hub/compare/v2.14.0...v2.14.1) (2020-04-09)


### Bug Fixes

* **Dependencies:** Upgrade Encoda to 0.93.6 ([005b7ee](https://github.com/stencila/hub/commit/005b7eeae94acc30f419a820b346928e57945333))

# [2.14.0](https://github.com/stencila/hub/compare/v2.13.1...v2.14.0) (2020-04-09)


### Features

* **Accounts:** Add theme and hosts to settings ([786ebc9](https://github.com/stencila/hub/commit/786ebc992ac09cd4b25e90ee2a243447e39c237f))
* **Accounts, Projects:** Add hosts and theme settings ([61f2aca](https://github.com/stencila/hub/commit/61f2acac948daf089ea6c8dbd221dd8051d0eba6))
* **Snapshots API:** Add list, create and retrieve views ([3d7d720](https://github.com/stencila/hub/commit/3d7d72009833a1d86ffae173ddb4f1f9f6b7b3b2))
* **Snapshots API:** Add view to retrieve a view in a particular format. ([4b29071](https://github.com/stencila/hub/commit/4b29071a18eb9bf3b163541f8c2f59ef608e0204))

## [2.13.1](https://github.com/stencila/hub/compare/v2.13.0...v2.13.1) (2020-04-07)


### Bug Fixes

* **Build:** Add !assets/*.py to .dockerignore ([a073486](https://github.com/stencila/hub/commit/a073486927a14dbf7900e0d68e180e120cb06521))
* **Build:** Write thema.py so that black will not format it ([b6448e6](https://github.com/stencila/hub/commit/b6448e6f29c4534f712a5cfd0f2a7810ba0dfa21))

# [2.13.0](https://github.com/stencila/hub/compare/v2.12.0...v2.13.0) (2020-04-07)


### Bug Fixes

* **Build:** Run prepare.js properly; avoid formatting generated files ([6e7c512](https://github.com/stencila/hub/commit/6e7c5125e074d119c1232ec988c76b5cc4882652))
* **Deps:** Upgrade Thema and Encoda version ([5a1c131](https://github.com/stencila/hub/commit/5a1c131d6199bc700d21184901605e811b027e4e))
* **Nodes:** Override default CamelCaseJSONParser ([c7de0c3](https://github.com/stencila/hub/commit/c7de0c3a67704d3ebe0add61e9d9a7f6783d4402))
* **Thema:** Use a specific version of Thema as a dependency. ([34b2460](https://github.com/stencila/hub/commit/34b24607f70f4a006a090e4709d3af806bf470a6)), closes [#367](https://github.com/stencila/hub/issues/367)


### Features

* **Nodes:** Add admin view ([1030ad4](https://github.com/stencila/hub/commit/1030ad4d66db5087a7ade3efa06efd6c43e46d1c))

# [2.12.0](https://github.com/stencila/hub/compare/v2.11.0...v2.12.0) (2020-04-06)


### Bug Fixes

* **Nodes:** Allow for node project being null ([939377a](https://github.com/stencila/hub/commit/939377a6d25b9d7c6174e6801627093b7a123422)), closes [#370](https://github.com/stencila/hub/issues/370)


### Features

* **Nodes:** Default app to api and add creator to complete HTMl view. ([24a1e12](https://github.com/stencila/hub/commit/24a1e1226f44abb6e5a2da3fa756a95793e806d3))

# [2.11.0](https://github.com/stencila/hub/compare/v2.10.0...v2.11.0) (2020-04-06)


### Bug Fixes

* **Account profile:** Revert to using pk ([47d79c0](https://github.com/stencila/hub/commit/47d79c08dd11741a9a2060a550ad31a6c4f5723a)), closes [/github.com/stencila/hub/pull/357#discussion_r403574787](https://github.com//github.com/stencila/hub/pull/357/issues/discussion_r403574787)
* **API URLs:** Place in seperate module ([6b4b840](https://github.com/stencila/hub/commit/6b4b840a3f4a2895e063757fc0e866e5f125c2df))
* **Nodes:** Add Encoda as a node creating app ([182a5a9](https://github.com/stencila/hub/commit/182a5a9e22ad84686a7a6960a4077b079aa12df8))
* **Nodes:** Add simple sign in message ([a9777f8](https://github.com/stencila/hub/commit/a9777f8f05990fda65692de750daafb540c66c54))
* **Pages titles:** Make more consistent ([c1efcf9](https://github.com/stencila/hub/commit/c1efcf9666c1949fdd60edde9c43f1d6619392cf))


### Features

* **Nodes:** Add app and doc fields; make serializers DRYer ([511c9b4](https://github.com/stencila/hub/commit/511c9b4e6c6787827f7db2f4340a451b0dce8537))
* **Nodes:** Add content for complete view ([d873c85](https://github.com/stencila/hub/commit/d873c85703e69651d32f2476e3b5cfb00de3bc28))
* **Nodes:** Add modes and API views for project nodes ([ad250f1](https://github.com/stencila/hub/commit/ad250f14e245d06f4f049e728180cc35d3e0d58c))
* **ProjectPermissionsMixin:** Add is_permitted method ([948a33e](https://github.com/stencila/hub/commit/948a33e20d449060a8392eb8d4d969de1b9b3810))

# [2.10.0](https://github.com/stencila/hub/compare/v2.9.5...v2.10.0) (2020-04-06)


### Bug Fixes

* **API docs:** Fix text and serve docs from /api ([1d4d1c2](https://github.com/stencila/hub/commit/1d4d1c23c87df5512ce59f7d1ca2b20854eb68bb))


### Features

* Passing current directory to GitHub link screen. Close [#366](https://github.com/stencila/hub/issues/366) ([7b3d56c](https://github.com/stencila/hub/commit/7b3d56cb66fcc9744d0a141173322ca7cdf67ec2))

## [2.9.5](https://github.com/stencila/hub/compare/v2.9.4...v2.9.5) (2020-04-05)


### Bug Fixes

* **Sign in:** Should respect the next parameter. Close [#368](https://github.com/stencila/hub/issues/368) ([cb5c1a9](https://github.com/stencila/hub/commit/cb5c1a97065f90ba2729625c8071d4ff9792601a))

## [2.9.4](https://github.com/stencila/hub/compare/v2.9.3...v2.9.4) (2020-04-04)


### Bug Fixes

* Showing message to contact support if Google token can't be refreshed. Fix [#352](https://github.com/stencila/hub/issues/352) ([8eda8e5](https://github.com/stencila/hub/commit/8eda8e5762b3ed1cf4e298f1faa3ec72b6c5ff5e))

## [2.9.3](https://github.com/stencila/hub/compare/v2.9.2...v2.9.3) (2020-04-04)


### Bug Fixes

* **deps:** update dependency django to v2.2.12 ([d3b9b40](https://github.com/stencila/hub/commit/d3b9b40435ba20ef133fb9b9f51c264ea9306373))
* **deps:** update dependency pillow to v7.1.1 ([e72021b](https://github.com/stencila/hub/commit/e72021b68e326e520fe4c4733dd3862d4f2283fd))

## [2.9.2](https://github.com/stencila/hub/compare/v2.9.1...v2.9.2) (2020-04-03)


### Bug Fixes

* Added !/general to .dockerignore ([a92a1a1](https://github.com/stencila/hub/commit/a92a1a1d16ff7784a9ec318d53c7d74de2ccd8f8))

## [2.9.1](https://github.com/stencila/hub/compare/v2.9.0...v2.9.1) (2020-04-03)


### Bug Fixes

* Fix for non-root Sources showing up in root directory, close [#358](https://github.com/stencila/hub/issues/358) ([d516908](https://github.com/stencila/hub/commit/d516908ce87cd5c3d71b8c49b4b8a9e722960c35))

# [2.9.0](https://github.com/stencila/hub/compare/v2.8.0...v2.9.0) (2020-04-02)


### Bug Fixes

* **API status:** Handle db connection error during deployment shutdown ([d24e796](https://github.com/stencila/hub/commit/d24e796e427cf15313eb912bf645ab2ed5641a0e)), closes [#336](https://github.com/stencila/hub/issues/336)


### Features

* **Admin:** Add dates to user admin list display ([f60b1af](https://github.com/stencila/hub/commit/f60b1afefed5662e7287c61b648255e326831ab1))

# [2.8.0](https://github.com/stencila/hub/compare/v2.7.1...v2.8.0) (2020-04-01)


### Bug Fixes

* **Policies:** Link to externally hosted policies ([3777d8b](https://github.com/stencila/hub/commit/3777d8be50302018d26a917bc5e522b4b33eb34c))


### Features

* **Analytics:** Adds PostHog integration ([61513ee](https://github.com/stencila/hub/commit/61513eeacf0ce2a33d9f313d578d84e0175fc89c))

## [2.7.1](https://github.com/stencila/hub/compare/v2.7.0...v2.7.1) (2020-04-01)


### Bug Fixes

* **Open:** Keep media files for JSON too ([0f68047](https://github.com/stencila/hub/commit/0f6804767c73e7e3b101c60e4b265b0458fe8e94))

# [2.7.0](https://github.com/stencila/hub/compare/v2.6.0...v2.7.0) (2020-04-01)


### Bug Fixes

* **Deps:** Upgrade Encoda to 0.94.3 ([6b0f815](https://github.com/stencila/hub/commit/6b0f8150ef67de3b738d03fb5ab7e842a1b2d6d2))
* **Open:** Revert to using main block ([732b045](https://github.com/stencila/hub/commit/732b045d6e2af53a4334b075077e56e23c509f2e))


### Features

* **Open:** Allow repro-PDFs to be uploaded ([660f347](https://github.com/stencila/hub/commit/660f3479dd9c4fd93d5e37e05ed317d48d43d5d6))

# [2.6.0](https://github.com/stencila/hub/compare/v2.5.4...v2.6.0) (2020-04-01)


### Bug Fixes

* Remove Pull Source Button ([bcf9fe7](https://github.com/stencila/hub/commit/bcf9fe764ecfc9097d3ef0876f6a5147a87f1c0e))
* Snapshot files button layout ([0ba06d3](https://github.com/stencila/hub/commit/0ba06d39299d5b30a948bded023dd969ef862cd4))


### Features

* Moved snapshot action into a modal and added tag ([18b2b94](https://github.com/stencila/hub/commit/18b2b9437b736ac890e9ba21fc3cad5cdd15514e))
* Removed standalone archives view and added zip downloading to snapshots ([d29e310](https://github.com/stencila/hub/commit/d29e3107d460b8b361ee0149aa6b53e949fe921a))

## [2.5.4](https://github.com/stencila/hub/compare/v2.5.3...v2.5.4) (2020-03-31)


### Bug Fixes

* **API Status:** Handle db connection error during warmup. ([cbb7f51](https://github.com/stencila/hub/commit/cbb7f511eb943ec967f1a110b0fb24bff05d66b3)), closes [#336](https://github.com/stencila/hub/issues/336)

## [2.5.3](https://github.com/stencila/hub/compare/v2.5.2...v2.5.3) (2020-03-31)


### Bug Fixes

* Fixed fetching of PublishedItem in preview, when the item has been previewed > once in snapshots. Close [#330](https://github.com/stencila/hub/issues/330) ([1a4ac5d](https://github.com/stencila/hub/commit/1a4ac5d143e2dee26b2e3179b9a349360f95fdeb))

## [2.5.2](https://github.com/stencila/hub/compare/v2.5.1...v2.5.2) (2020-03-31)


### Bug Fixes

* Deleting PublishedItem when its Source is deleted, fix [#335](https://github.com/stencila/hub/issues/335) ([838f753](https://github.com/stencila/hub/commit/838f7537476a14652018ec647c8e3e248890f7f8))

## [2.5.1](https://github.com/stencila/hub/compare/v2.5.0...v2.5.1) (2020-03-30)


### Bug Fixes

* **Open:** Replace beta signup with signin ([5bee7c3](https://github.com/stencila/hub/commit/5bee7c3275a41e1dc6013794e22ddb7620a0a33c))
* **Themes:** Upgrade to Thema 1.16 ([0c0b9c0](https://github.com/stencila/hub/commit/0c0b9c0a9c4a941425e89c2533a73820090918b8))

# [2.5.0](https://github.com/stencila/hub/compare/v2.4.1...v2.5.0) (2020-03-30)


### Bug Fixes

* **Deps:** Update Encoda to 0.93.2 ([12a2ea9](https://github.com/stencila/hub/commit/12a2ea928450b1e247810e1b8110dae629f96ab6))


### Features

* **Open:** Add PDF download; improve styling ([29ec6bf](https://github.com/stencila/hub/commit/29ec6bf14d62f85c3a56a4674d1e52fc744feab3))
* **Open:** Allow opening of eLife and PLoS JATS articles ([91af886](https://github.com/stencila/hub/commit/91af88608581645aa071694efebf39eaf37fefc4))
* **Open:** Integrate /open into main app ([67f056f](https://github.com/stencila/hub/commit/67f056fd4803c38e07924171027d11e2d9dc376f))

## [2.4.1](https://github.com/stencila/hub/compare/v2.4.0...v2.4.1) (2020-03-30)


### Bug Fixes

* **Error page:** Fix typo and in the process rewrite text ([6322f71](https://github.com/stencila/hub/commit/6322f71f42ce79f15d8ab0a2777d80125a63b0aa))
* **Error page:** Fix typo and in the process rewrite text [skip ci] ([474f7ff](https://github.com/stencila/hub/commit/474f7ff219db041432c1f4d2246bd6c124773891))
* **Project admin:** Remove obsolete archive field. ([15e4322](https://github.com/stencila/hub/commit/15e432236da2c69a4ad85d1965ede69a2eceee10))

# [2.4.0](https://github.com/stencila/hub/compare/v2.3.5...v2.4.0) (2020-03-29)


### Bug Fixes

* **Error logging:** Upgrade to sentry-sdk; use message for migrations, not exception ([89b64c6](https://github.com/stencila/hub/commit/89b64c61cf613c8feb301146edb23a461f153e3d)), closes [#336](https://github.com/stencila/hub/issues/336) [#350](https://github.com/stencila/hub/issues/350)


### Features

* **Error page:** Improve 500 page and add feedback form ([9c5555c](https://github.com/stencila/hub/commit/9c5555cacbe0a7200530d1c80a9b371bf9bfdbd1)), closes [#69](https://github.com/stencila/hub/issues/69)

## [2.3.5](https://github.com/stencila/hub/compare/v2.3.4...v2.3.5) (2020-03-29)


### Bug Fixes

* **deps:** update dependency django-avatar to v5 ([a7206b9](https://github.com/stencila/hub/commit/a7206b9446d5bb9682730e394ad81e993cbbdbf1))
* **deps:** update dependency pillow to v7 ([2102769](https://github.com/stencila/hub/commit/21027690f651baee722bf56a06495c99b87c1645))
* **deps:** update dependency shortuuid to v1 ([0150a58](https://github.com/stencila/hub/commit/0150a58ac98ae70e64d714d2605e0a408bee39d3))

## [2.3.4](https://github.com/stencila/hub/compare/v2.3.3...v2.3.4) (2020-03-29)


### Bug Fixes

* **deps:** update dependency django-extensions to v2.2.9 ([91636ac](https://github.com/stencila/hub/commit/91636ac2a248f5e9d358d8710569bc74184c8c77))
* **deps:** update dependency pillow to v6.2.2 ([0f3dd8d](https://github.com/stencila/hub/commit/0f3dd8d3e8c7c10be9773c1e1320efebe563e94e))
* **deps:** update dependency psycopg2-binary to v2.8.4 ([e6abb14](https://github.com/stencila/hub/commit/e6abb14d0279b8d39cf337548b4ffa77b2d514ef))
* **deps:** update dependency requests to v2.23.0 ([4458a23](https://github.com/stencila/hub/commit/4458a234cfb4951404a302fadca45e869d5fa4c8))

## [2.3.3](https://github.com/stencila/hub/compare/v2.3.2...v2.3.3) (2020-03-29)


### Bug Fixes

* **File browser:** Improve consistency in delete, unlink and rename modals ([c584c66](https://github.com/stencila/hub/commit/c584c664d910d1336c51393c7e575a45eb994448))
* **File browser:** Open all files in a new window ([626682d](https://github.com/stencila/hub/commit/626682d8ca0d7685e1649e123c4a0f7c0ea19544))
* **File browser:** Simplify filename conflict notif; fade away on rename ([60e2754](https://github.com/stencila/hub/commit/60e2754e23c8c5b15b8af2554cd84cccd30ad01a))
* **File browser:** Simplify Save As modal ([2a89b95](https://github.com/stencila/hub/commit/2a89b95750f7251d21d8fceee6a386056ed23b9d))
* **Open:** Remove Executa as unused. ([faa0bc0](https://github.com/stencila/hub/commit/faa0bc0204b8d38136b438c1482461ca43b26ddb)), closes [#349](https://github.com/stencila/hub/issues/349)
* Redesign file action menu with Save As Other ([752be4b](https://github.com/stencila/hub/commit/752be4bccaea60a1d806d3463cbfee5b2db13504))

## [2.3.2](https://github.com/stencila/hub/compare/v2.3.1...v2.3.2) (2020-03-28)


### Bug Fixes

* Create team view, fix [#337](https://github.com/stencila/hub/issues/337) ([d6b3a95](https://github.com/stencila/hub/commit/d6b3a954038faebd5a46d3d21975f21435ceb26f))

## [2.3.1](https://github.com/stencila/hub/compare/v2.3.0...v2.3.1) (2020-03-26)


### Bug Fixes

* **Open:** Correct elife theme name ([f05f766](https://github.com/stencila/hub/commit/f05f766b528d2ec86ea26fc6ccfe188b65b68ea6))

# [2.3.0](https://github.com/stencila/hub/compare/v2.2.1...v2.3.0) (2020-03-25)


### Bug Fixes

* **Deps:** Upgrade Thema to 1.15.1 ([51abf87](https://github.com/stencila/hub/commit/51abf879fb549bc4860fbb823dba956a95cc883e))


### Features

* **File preview:** Allow theme to be set using query parameter ([4297492](https://github.com/stencila/hub/commit/42974927ab7a867105e8c50f64d34209283da77f))

## [2.2.1](https://github.com/stencila/hub/compare/v2.2.0...v2.2.1) (2020-03-25)


### Bug Fixes

* **Deps:** Upgrade Encoda to 0.92.0 ([944c440](https://github.com/stencila/hub/commit/944c440fe1f258b88b1b630572869695ca372870))

# [2.2.0](https://github.com/stencila/hub/compare/v2.1.0...v2.2.0) (2020-03-25)


### Bug Fixes

* **API docs:** Improve  styling of docs ([2cf112a](https://github.com/stencila/hub/commit/2cf112abe55869aa7f1d138e5a85ba55863ec2ba))


### Features

* Account Admin users now get OWN permission on projects in their Account ([e9bb00c](https://github.com/stencila/hub/commit/e9bb00c6912b9ed348f01f90b0d7f6c244ae0298))

# [2.1.0](https://github.com/stencila/hub/compare/v2.0.3...v2.1.0) (2020-03-25)


### Features

* **API:** Add endpoints for managing authentication tokens. ([3ef9233](https://github.com/stencila/hub/commit/3ef9233f36c1167c9364ffcda899249b75f0208a))

## [2.0.3](https://github.com/stencila/hub/compare/v2.0.2...v2.0.3) (2020-03-25)


### Bug Fixes

* **Deps:** Upgrade to using Python 3.7 and Ubuntu 19.10 ([33f5ba1](https://github.com/stencila/hub/commit/33f5ba1e27cac068bb3c807bd6dd7a193cafa8ba))

## [2.0.2](https://github.com/stencila/hub/compare/v2.0.1...v2.0.2) (2020-03-24)


### Bug Fixes

* Manually returning 200 OK for GoogleHC user agents ([765026c](https://github.com/stencila/hub/commit/765026cd78a4e4583c5d3b40333f42e3e97b5528))

## [2.0.1](https://github.com/stencila/hub/compare/v2.0.0...v2.0.1) (2020-03-24)


### Bug Fixes

* **Settings:** Update path to status check ([650c44d](https://github.com/stencila/hub/commit/650c44d68140809be7f74ccffc6b3e09b19f29f5))

# [2.0.0](https://github.com/stencila/hub/compare/v1.1.1...v2.0.0) (2020-03-24)


### Bug Fixes

* **Settings:** Do not require beta token setting in prod ([623aafb](https://github.com/stencila/hub/commit/623aafb2732fc5a01a0691d0c62c78c08148dc50))


### Features

* **API:** Use camel casing; return more user details when granting auth token. ([93c1900](https://github.com/stencila/hub/commit/93c190063927ad903b60f159f7f4ca38b11188ff))


### BREAKING CHANGES

* **API:** change to camelCasing may break existing API clients

## [1.1.1](https://github.com/stencila/hub/compare/v1.1.0...v1.1.1) (2020-03-23)


### Bug Fixes

* **deps:** update dependency google-api-python-client to v1.8.0 ([276935b](https://github.com/stencila/hub/commit/276935bfa5a4701ef72af4b000de82ba07d139c9))

# [1.1.0](https://github.com/stencila/hub/compare/v1.0.0...v1.1.0) (2020-03-23)


### Bug Fixes

* **Settings:** Use unpkg.com CDN in prod ([44177be](https://github.com/stencila/hub/commit/44177be9ba2ec3fa985573c91598f0763bf82209))

# [1.0.0](https://github.com/stencila/hub/compare/v1.0.0...v0.9.2) (2020-03-23)


### Bug Fixes

* **Deps:** Django extensions is prod dep ([4c22046](https://github.com/stencila/hub/commit/4c22046427dc1b22476d4a7d8086a752ad240461))

## [0.9.2](https://github.com/stencila/hub/compare/v0.9.1...v0.9.2) (2020-03-23)


### Bug Fixes

* **deps:** update dependency django to v2.2.11 ([65a3ede](https://github.com/stencila/hub/commit/65a3ede36e0678b63a057e8bb0ad8d9092c88e79))
* **deps:** update dependency django-allauth to v0.41.0 ([924a9fa](https://github.com/stencila/hub/commit/924a9fa0a547c3a154ca1ae96d11336ca99f10fd))
* **deps:** update dependency django-configurations to v2.2 ([2b55b7e](https://github.com/stencila/hub/commit/2b55b7e5d4aca669edf844f9beabdd3c35e61467))
* **deps:** update dependency django-crispy-forms to v1.9.0 ([22be7ab](https://github.com/stencila/hub/commit/22be7ab1a05a9d252488f851d5ca5c5f34f6ffc0))
* **User search:** Account for change in API ([3ed7c73](https://github.com/stencila/hub/commit/3ed7c7303c0f9ba1fa0813a835d850bc362f6d02))
* **User search API:** Add additional fields to result and alter fields searched ([8211723](https://github.com/stencila/hub/commit/8211723c1603ecc6a3ad5cdd853c6342fad5bda2))

## [0.9.1](https://github.com/stencila/hub/compare/v0.9.0...v0.9.1) (2020-03-21)


### Bug Fixes

* **deps:** update dependency dj-stripe to v2.2.3 ([cb0f725](https://github.com/stencila/hub/commit/cb0f72594ef09d57525d93b76fad64d1128f2c96))
* **deps:** update dependency django-debug-toolbar to v2.2 ([ec71452](https://github.com/stencila/hub/commit/ec71452d543175be8feba553e131bd96d214b37c))
* **deps:** update dependency django-extensions to v2.2.8 ([34baf19](https://github.com/stencila/hub/commit/34baf1926e637ab5d09ed918f402a0f28c3011b2))
* **deps:** update dependency django-intercom to v0.1.3 ([1d117f2](https://github.com/stencila/hub/commit/1d117f2269ae1ffeba78bb0e08228ef4c59d4b90))
* **deps:** update dependency django-sendgrid-v5 to v0.8.1 ([3c746e5](https://github.com/stencila/hub/commit/3c746e59acbb01d87856b643901c58a91dc91239))
* **Deps:** Update stencila-schema ([a50bd30](https://github.com/stencila/hub/commit/a50bd3068e97cb6cd26fb61268a9594293e50a80))

# [0.9.0](https://github.com/stencila/hub/compare/v0.8.27...v0.9.0) (2020-03-21)


### Bug Fixes

* **API:** Normalize API errors ([699c190](https://github.com/stencila/hub/commit/699c190c5c94d4f878451b6b1b13f72b1217ce73))
* **API Auth:** Remove JWTs as an authorization option ([a4ab72e](https://github.com/stencila/hub/commit/a4ab72e981c98915bb701c527dcccf1253ad58ba))
* **API docs:** Ensure schema is publically accessible; hide auth buttin in swagger ([fe5a5ad](https://github.com/stencila/hub/commit/fe5a5adcf2005189d2d6ea7115459ab463ddf5bf))
* **API docs:** Hide routes not being reviewed in this round ([787d3c5](https://github.com/stencila/hub/commit/787d3c5ac6d249a25f4026b39f7baf4329c0fef3))
* **API URLs:** Allow optional trailing slash ([c12117d](https://github.com/stencila/hub/commit/c12117d5ba16dfaf9efb78bd1bdddc8f3a9e4e8a))
* **File browser:** Remove reference to removed function ([c019242](https://github.com/stencila/hub/commit/c019242429184ce560757120b8c64cb2e2a49fc9))
* Filtering by project event status ([3cdf138](https://github.com/stencila/hub/commit/3cdf13809828a9a82d9e73f89e22bb2677de4b3e))
* Record status for completed SNAPSHOT events. ([30824b3](https://github.com/stencila/hub/commit/30824b3ffc8599ae4d7c3bb307c8cce36ac8ef08))
* Recording ProjectEvents for anonymous users ([2d479e4](https://github.com/stencila/hub/commit/2d479e43ee81cef085b46a9b5e325299e778445d))
* Remove pesudo-terminal code from page overview ([4ac79e0](https://github.com/stencila/hub/commit/4ac79e01f822ad71acaff59dd3549a0515fc0978))
* **Migrations:** Remove the reference to the deleted checkouts app ([51557d5](https://github.com/stencila/hub/commit/51557d5b2a19d9442c94f6917b81af886ec858a0))


### Features

* **API:** Add and document additional project fields ([8032f6e](https://github.com/stencila/hub/commit/8032f6e366d582dd6c917efced11a129b23dff28))
* **API:** Complete initial OpenID JWT granting ([df224f6](https://github.com/stencila/hub/commit/df224f6adb1e69ffb543946cc2ccf9cfcd339009))
* **API:** Use knox to provide user authentication tokens "UATs" ([e836525](https://github.com/stencila/hub/commit/e836525c784fd12ace1ea9d97771e396c7f4d4b3))
* **API Tokens:** Allow for refreshing and revoking both token types ([edf2f4e](https://github.com/stencila/hub/commit/edf2f4e91aa4f57492d082a2257c2d2505fb3be8))
* **API Tokens:** Generate JWT token from Google auth JWT ([23b0e3e](https://github.com/stencila/hub/commit/23b0e3ea737d6c7e820011c51eabd0d59f9af4b5))
