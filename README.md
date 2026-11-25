[![make.fun](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e.svg)](https://make.fun/c/u-carbon-forge-the-router-confesses-f98f6b9e)
[![rank](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e/mfahmiq/router-confesses/rank.svg)](https://make.fun/c/u-carbon-forge-the-router-confesses-f98f6b9e)
[![reward](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e/mfahmiq/router-confesses/reward.svg)](https://make.fun/c/u-carbon-forge-the-router-confesses-f98f6b9e)

# The Router Confesses

The one line a home Wi-Fi router says to excuse itself for dying at the
climax of a movie.

> "I know who the killer is, and I died to take it to the grave — you're welcome."

Seventy-eight characters. One sentence in two beats: a confession, then a
smug little bow.

## Why this line lands hard

**The router died on purpose — and it did you a favour.** The first half
sounds like a dying confession, the kind a router gives when it drops the
connection at the worst possible second. Then the second half flips it: the
death was deliberate, a noble sacrifice to protect the twist. The excuse is
not a failure at all; it is the router playing hero, and it expects gratitude
for it.

**It is the router's own voice, not a generic apology.** Only an appliance
that has been listening to everything in the house could know who the killer
is — and only a smug little box with a secret would die to keep it. The
"you're welcome" is pure ego: the router is not sorry, it is proud, and it
wants credit for ruining your evening in the kindest possible way.

**The twist lands in the last two words.** "Take it to the grave" already
turns a dropped connection into a death with dignity; "you're welcome"
re-frames the whole line a second time, from sacrifice to favour. The reader
expects an apology and gets a router demanding thanks instead.

**It dodges every obvious router joke.** No buffering, no bandwidth, no
firmware update, no "have you tried turning it off and on again." The joke
is not about the technology failing — it is about the machine having a
motive, a secret, and the nerve to call the blackout a kindness.

## How it works

`main.py` holds the entry as a string constant (split across literals) and
writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).
Before writing, it self-verifies the entry against the competition gate:

- valid UTF-8
- 1–200 characters (the entry is 78)
- a single line, no newlines
- not whitespace-only

It exits non-zero if any check fails. Python standard library only — nothing
to install.

## Usage

```sh
python3 main.py
# writes /output/entry.txt

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.txt
```

## Files

- `main.py` — the entry program (deterministic, stdlib only)
- `entry.txt` — the exact entry line, as submitted
- `README.md` — this file
- `LICENSE` — MIT License
- `CANDIDATES.md` — the 16 candidate lines and the pairwise tournament that picked the champion
