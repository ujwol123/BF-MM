import mnemonic

# Generate a random seed with 128 bits of entropy
entropy = mnemonic.entropy.generate(128)

# Convert the entropy to a 12-word seed phrase
mnemo = mnemonic.Mnemonic("english")
seed_phrase = mnemo.to_mnemonic(entropy, wordlist='english', strength=128)

print(seed_phrase)
