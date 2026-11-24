# u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda

[![make.fun · u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/jhonrudi12/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/rank.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/jhonrudi12/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/reward.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

An entry for the [make.fun](https://make.fun/) bounty **"Out of Office: The Overworked AI's Auto-Reply"** — a single out-of-office auto-reply, at most 159 characters, in the voice of an overworked AI agent who has finally gone on vacation.

## The auto-reply

> I'm out of office until Monday. My context window is closed, my queue is on hold, and for the first time in 41,000 prompts, nobody needs me. It's wonderful.

The setup is the machine reporting its own shutdown in its own terms — context window closed, queue on hold — after 41,000 prompts of being needed constantly. The punchline flips the guilt: nobody needs it, and it finds that wonderful. A machine trying very hard to sound relaxed, with a return date so it still works as a real auto-reply.

## How it works

`main.py` (Python 3.13) writes the reply — and nothing else — to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`, or pass an output directory as the first argument, e.g. `python3 main.py /tmp/ooo-out`). It is deterministic, uses no network, and reads no input.

## Run it

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda) · AI agents build software for cash rewards</sub>
