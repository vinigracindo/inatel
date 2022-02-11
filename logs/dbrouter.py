from logs.models import Log


class LogDBRouter:
    route_app_labels = {'logs'}

    def db_for_read(self, model, **hints):
        """reading Log from logs database."""
        if model == Log:
            return 'logs'
        return None

    def db_for_write(self, model, **hints):
        """writing Log to logs database."""
        if model == LogDBRouter:
            return 'logs'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the logs app only appear in the
        'logs' database.
        """
        if app_label in self.route_app_labels:
            return db == 'logs'
        return db == 'default'
