# Password Strength Checker

A beginner-friendly Python cybersecurity project that analyzes a password and provides a simple strength classification and improvement suggestions.

## Features

- Checks whether the password is empty.
- Checks password length.
- Detects uppercase letters.
- Detects lowercase letters.
- Detects numbers.
- Detects special characters.
- Detects common passwords.
- Calculates a simple score from 0 to 5.
- Classifies the password as Weak, Medium, or Strong.
- Provides suggestions for improving the password.

## Technology

- Python 3
- Developed and tested with Pydroid 3 on Android.

## How the Scoring Works

The password receives one point for each condition:

1. At least 8 characters
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one number
5. At least one special character

A password in the common-password list is classified as Weak even if its structural score is high.

## Example

Input:

`Ahmed@123`

Output:

```text
Score: 5
Password Strength: Strong
