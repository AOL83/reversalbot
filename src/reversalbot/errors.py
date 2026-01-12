"""Custom exceptions for ReversalBot."""


class ReversalBotError(Exception):
    """Base error for ReversalBot."""


class RiskViolationError(ReversalBotError):
    """Raised when a risk check fails."""


class KillSwitchEngagedError(ReversalBotError):
    """Raised when an action is blocked by kill switch."""


class PauseEngagedError(ReversalBotError):
    """Raised when an action is blocked by pause control."""
