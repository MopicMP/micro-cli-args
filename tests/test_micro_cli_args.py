"""Tests for micro-cli-args."""

import pytest
from micro_cli_args import args


class TestArgs:
    """Test suite for args."""

    def test_basic(self):
        """Test basic usage."""
        result = args("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            args("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = args(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
