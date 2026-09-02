# Discord Selfbot

A simple Discord selfbot with only a `.ping` command (owner-only).

⚠️ **WARNING**: Using selfbots violates Discord's Terms of Service. Use at your own risk.

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure the Bot
Edit `main.py` and update:
- `OWNER_IDS`: Replace `[123456789]` with your Discord user ID
- `TOKEN`: Replace `"YOUR_DISCORD_TOKEN_HERE"` with your account token

### 3. Get Your User ID
Right-click your profile → Copy User ID (requires Developer Mode enabled)

### 4. Get Your Token
- Open Discord in your browser
- Press F12 (Developer Tools)
- Go to Application → Cookies → Select discord.com
- Find the `token` cookie and copy its value

### 5. Run the Bot
```bash
python main.py
```

## Commands

- `.ping` - Shows bot latency (owner-only)

## Features

✅ Owner-only command execution
✅ Message deletion for unauthorized users
✅ Latency calculation
✅ Embed responses

## ⚠️ Disclaimer

This selfbot is provided for educational purposes only. Unauthorized automation of Discord accounts may result in:
- Account suspension
- Permanent ban from Discord
- Violation of Discord ToS

Use responsibly!
