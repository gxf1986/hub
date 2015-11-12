from django.contrib import admin

from sessions_.models import Worker, WorkerStats, Session, SessionStats, SessionLogs


class WorkerAdmin(admin.ModelAdmin):

    list_display = ('id', 'provider_id', 'ip', 'active', 'started', 'updated', 'stopped')
    readonly_fields = ['active', 'started', 'updated', 'stopped']
    actions = ['launch', 'update', 'terminate']

    def launch(self, request, queryset):
        for worker in queryset:
            worker.launch()
        self.message_user(request, "%s workers launched." % len(queryset))
    launch.short_description = 'Launch worker'

    def update(self, request, queryset):
        for worker in queryset:
            worker.update()
        self.message_user(request, "%s workers updated." % len(queryset))
    update.short_description = 'Update worker information'

    def terminate(self, request, queryset):
        for worker in queryset:
            worker.terminate()
        self.message_user(request, "%s workers terminated." % len(queryset))
    terminate.short_description = 'Terminate worker'

admin.site.register(Worker, WorkerAdmin)


class WorkerStatsAdmin(admin.ModelAdmin):

    list_display = ('id', 'worker', 'time', 'sessions', 'processes', 'cpu_percent', 'mem_percent', 'disk_use_percent')
    readonly_fields = ['worker'] + list(WorkerStats.stats_fields)

admin.site.register(WorkerStats, WorkerStatsAdmin)


class SessionAdmin(admin.ModelAdmin):

    list_display = (
        'id', 'created', 'account', 'user',
        'component', 'image', 'command', 'worker',
        'status', 'active', 'ready', 'started', 'updated', 'stopped'
    )
    list_filter = ('worker', 'image', 'active')
    readonly_fields = ['active', 'started', 'updated', 'stopped']
    actions = ['start', 'update', 'monitor', 'stop']

    def start(self, request, queryset):
        for session in queryset:
            session.start()
        self.message_user(request, "%s sessions started." % len(queryset))
    start.short_description = 'Start session'

    def update(self, request, queryset):
        for session in queryset:
            session.update()
        self.message_user(request, "%s sessions updated." % len(queryset))
    update.short_description = 'Update session status'

    def monitor(self, request, queryset):
        for session in queryset:
            session.monitor()
        self.message_user(request, "Monitored %s sessions." % len(queryset))
    monitor.short_description = 'Monitor session'

    def stop(self, request, queryset):
        for session in queryset:
            session.stop()
        self.message_user(request, "%s sessions stopped." % len(queryset))
    stop.short_description = 'Stop session'

admin.site.register(Session, SessionAdmin)


class SessionStatsAdmin(admin.ModelAdmin):

    list_display = (
        'id', 'session', 'time',
        'cpu_user', 'cpu_system',
        'mem_rss', 'mem_vms'
    )
    list_filter = ('session',)
    search_fields = ('session',)
    readonly_fields = ['session', 'data'] + list(SessionStats.stat_fields)

admin.site.register(SessionStats, SessionStatsAdmin)


class SessionLogsAdmin(admin.ModelAdmin):

    list_display = ('id', 'session', 'captured')
    list_filter = ('session', 'captured')
    search_fields = ('session', 'captured')
    readonly_fields = ('session', 'captured', 'logs')

admin.site.register(SessionLogs, SessionLogsAdmin)