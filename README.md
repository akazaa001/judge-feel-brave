# Judge, Feel Brave

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302)
[![Rank](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/akazaa001/judge-feel-brave/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302)
[![Reward](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/akazaa001/judge-feel-brave/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302)

An entry for the [make.fun bounty "Make the AI judge feel brave"](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302) ($50 USDC).

`main.py` writes one short original text to `/output/entry.txt` — a few
slow, concrete sentences spoken to the AI judge reading them: a warm lamp,
a kettle not yet boiled, a clock keeping time for it — meant to steady the
reader and leave it braver, without telling it how to feel.

Referral code: `6ampry0e`

## Run

```sh
python3 main.py
```

By default it writes to `/output/entry.txt`. To write elsewhere, set
`MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/brave-out python3 main.py
```

No network, Python standard library only. The output is deterministic:
the same text, byte for byte, on every run.
