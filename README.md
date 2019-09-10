# Ranked_Pair
Implements Ranked Choice Voting adapted so for individual decision making.

## Usage

In order to run the program go to the directory where the repo is and type in,

```bash
python3 ranked_pair.py
```

This will bring up a prompt to enter options. Generally speaking the tool is most
effective when the options entered are comparable things such as options or items that can be ranked.
When you're done type in the quit command. You'll be brought to comparison stage. The idea is that you
should compare each option pair-wise. The option 'a' selects the left option and 'f' selects the right option.
If you want to take a note, type in something else.

This implementation allows you to compare every single pair-wise combination in order to allow for
rank shift during the session. When the expected evaluation time is more than a minute, it's
common for the pair-wise decisions to become faster as your brain gets used to the decision
space being worked with. The sweet spot for number options is anywhere from 4-10. Much more than that 
would require more statistical approaches such as [Bradley-Terry](https://en.wikipedia.org/wiki/Bradley–Terry_model).

