#!/usr/bin/env python3
"""
Validate that production secrets have been changed from defaults
Run this script before deploying to production
"""

import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import DATABASE, SECRET_KEY, SESSION_SECRET, ENVIRONMENT


def validate_secrets():
    """Validate that all secrets have been changed from defaults"""
    errors = []
    warnings = []

    print("🔒 Validating Production Secrets...")
    print("=" * 60)

    # Check JWT secret
    if SECRET_KEY == 'change_this_to_a_random_secret_key':
        errors.append("❌ JWT_SECRET is still set to default value!")
        print("  JWT_SECRET: ❌ DEFAULT (MUST CHANGE)")
    elif len(SECRET_KEY) < 32:
        warnings.append("⚠️  JWT_SECRET is less than 32 characters (recommended: 32+)")
        print("  JWT_SECRET: ⚠️  TOO SHORT")
    else:
        print("  JWT_SECRET: ✅ CHANGED")

    # Check session secret
    if SESSION_SECRET == 'change_this_to_another_random_secret':
        errors.append("❌ SESSION_SECRET is still set to default value!")
        print("  SESSION_SECRET: ❌ DEFAULT (MUST CHANGE)")
    elif len(SESSION_SECRET) < 32:
        warnings.append("⚠️  SESSION_SECRET is less than 32 characters (recommended: 32+)")
        print("  SESSION_SECRET: ⚠️  TOO SHORT")
    else:
        print("  SESSION_SECRET: ✅ CHANGED")

    # Check database password
    default_passwords = [
        'vnstock_password_change_in_production',
        'password',
        '123456',
        'admin'
    ]
    if DATABASE['password'] in default_passwords:
        errors.append("❌ DB_PASSWORD is set to a default/weak value!")
        print("  DB_PASSWORD: ❌ DEFAULT/WEAK (MUST CHANGE)")
    elif len(DATABASE['password']) < 12:
        warnings.append("⚠️  DB_PASSWORD is less than 12 characters (recommended: 16+)")
        print("  DB_PASSWORD: ⚠️  TOO SHORT")
    else:
        print("  DB_PASSWORD: ✅ SECURE")

    # Check environment
    print(f"\n  Environment: {ENVIRONMENT}")

    print("=" * 60)

    # Print warnings
    if warnings:
        print("\n⚠️  WARNINGS:")
        for warning in warnings:
            print(f"  {warning}")

    # Print errors and exit with status
    if errors:
        print("\n❌ VALIDATION FAILED:")
        for error in errors:
            print(f"  {error}")
        print("\n🛠️  How to fix:")
        print("  1. Update your .env file with secure random values")
        print("  2. Use: python -c \"import secrets; print(secrets.token_hex(32))\"")
        print("  3. Re-run this script to validate")
        print()
        return False
    else:
        if warnings and ENVIRONMENT == 'production':
            print("\n⚠️  Secrets are changed but some warnings remain")
            print("   Consider addressing warnings for production deployment")
        else:
            print("\n✅ All secrets are properly configured!")
        return True


if __name__ == '__main__':
    success = validate_secrets()
    sys.exit(0 if success else 1)
