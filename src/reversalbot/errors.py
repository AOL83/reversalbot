class ReversalBotError(Exception):
    """Base error for ReversalBot."""


class KillSwitchEngagedError(ReversalBotError):
    """Raised when the kill switch is engaged."""


class RouterPausedError(ReversalBotError):
    """Raised when routing is paused."""
