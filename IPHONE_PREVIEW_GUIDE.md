# 📱 How to Preview on Your iPhone/iPad

## Quick Start Guide

### Step 1: Find Your Computer's IP Address

**On Windows (PowerShell):**
```powershell
ipconfig | findstr IPv4
```

**Look for something like:**
- `192.168.1.XXX` (most common)
- `10.0.0.XXX`
- `172.16.XXX.XXX`

### Step 2: Make Sure Flask is Running

Your Flask app should be running with:
```bash
python app.py
```

**IMPORTANT**: Flask must be accessible on your network. By default, Flask only runs on `localhost` (127.0.0.1), which won't work for mobile devices.

### Step 3: Update Flask to Listen on All Interfaces

**Option A: Modify app.py temporarily**

Find this line in `app.py`:
```python
app.run(debug=True)
```

Change it to:
```python
app.run(host='0.0.0.0', port=5000, debug=True)
```

**Option B: Run with command line argument**
```bash
python app.py --host=0.0.0.0
```

### Step 4: Allow Firewall Access

**Windows Firewall:**
1. Open Windows Defender Firewall
2. Click "Allow an app through firewall"
3. Find Python or allow port 5000
4. Check both Private and Public networks

**Quick PowerShell command (Run as Administrator):**
```powershell
New-NetFirewallRule -DisplayName "Flask Dev Server" -Direction Inbound -LocalPort 5000 -Protocol TCP -Action Allow
```

### Step 5: Connect from iPhone/iPad

1. **Make sure your iPhone and computer are on the SAME Wi-Fi network**
2. Open Safari on your iPhone
3. Type in the address bar: `http://YOUR_IP:5000`
   - Example: `http://192.168.1.100:5000`
4. Press Go

### Step 6: Add to Home Screen (Optional)

For the best app-like experience:
1. Tap the Share button (square with arrow)
2. Scroll down and tap "Add to Home Screen"
3. Name it "OS Assistant"
4. Tap "Add"
5. Open from your home screen!

## Troubleshooting

### ❌ "Can't connect" or "Safari cannot open the page"

**Check 1: Same Network**
- iPhone and computer must be on the same Wi-Fi
- Don't use VPN on either device

**Check 2: Firewall**
- Windows Firewall might be blocking port 5000
- Temporarily disable firewall to test

**Check 3: Flask Host**
- Make sure Flask is running with `host='0.0.0.0'`
- Restart Flask after making changes

**Check 4: Correct IP**
- Double-check your computer's IP address
- IP might change if you reconnect to Wi-Fi

### ❌ "Connection refused"

Flask is not running or not listening on 0.0.0.0:
```bash
# Stop Flask (Ctrl+C)
# Restart with:
python app.py
```

### ❌ Page loads but looks broken

- Hard refresh on iPhone: Pull down to refresh
- Clear Safari cache: Settings → Safari → Clear History and Website Data

## Alternative: Use ngrok (Internet Access)

If local network doesn't work, use ngrok for a public URL:

1. Download ngrok: https://ngrok.com/download
2. Run Flask normally: `python app.py`
3. In another terminal: `ngrok http 5000`
4. Copy the https URL (e.g., `https://abc123.ngrok.io`)
5. Open that URL on your iPhone

**Pros:**
- Works from anywhere
- No firewall issues
- HTTPS (more secure)

**Cons:**
- Requires internet
- URL changes each time
- Free tier has limits

## Quick Test

Before trying on iPhone, test from your computer:

1. Open browser on your computer
2. Go to `http://YOUR_IP:5000` (use your actual IP)
3. If it works here, it should work on iPhone

## Example Setup

```bash
# 1. Find IP
ipconfig
# Result: 192.168.1.105

# 2. Start Flask
python app.py
# Should show: Running on http://0.0.0.0:5000

# 3. On iPhone Safari
# Go to: http://192.168.1.105:5000
```

## What You Should See on iPhone

✅ **Success looks like:**
- Clean chat interface loads
- Sidebar menu works
- Can type and send messages
- Smooth animations
- No zoom when typing
- Looks native and professional

❌ **Problems look like:**
- "Cannot connect to server"
- "Safari cannot open the page"
- Blank white screen
- Desktop layout (too zoomed out)

## Need Help?

1. Verify Flask is running: Check terminal for errors
2. Verify IP is correct: Run `ipconfig` again
3. Verify same network: Check Wi-Fi name on both devices
4. Verify firewall: Temporarily disable to test
5. Try ngrok: If all else fails

---

**Pro Tip**: Once you get it working, bookmark the URL on your iPhone for easy access!
