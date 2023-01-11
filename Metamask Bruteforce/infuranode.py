import mnemonic
from mnemonic import Mnemonic
from eth_keys import keys
from web3 import Web3

while True:
    # Generate a random seed with 128 bits of entropy
    entropy = mnemonic.entropy.generate(128)

    # Convert the entropy to a 12-word seed phrase
    mnemo = mnemonic.Mnemonic("english")
    seed_phrase = mnemo.to_mnemonic(entropy, wordlist='english', strength=128)

    # Check if seed phrase is valid
    def is_valid_seed_phrase(seed_phrase):
        try:
            Mnemonic.check(seed_phrase)
            return True
        except:
            return False

    if is_valid_seed_phrase(seed_phrase):
        # Generate private key from seed phrase
        private_key = keys.PrivateKey.from_mnemonic(seed_phrase)

        # Get corresponding address
        address = private_key.public_key.to_address()

        # Function to check if address has a balance on the Ethereum blockchain
        def get_balance(address):
            w3 = Web3(Web3.HTTPProvider("http://mainnet.infura.io/v3/your_project_id"))
            return w3.eth.getBalance(address)

        # Check if address has a balance on the Ethereum blockchain
        balance = get_balance(address)

        if balance > 0:
            with open("valid_seed_phrases.txt", "a") as f:
                f.write(seed_phrase+"\n")
            print("Seed phrase corresponds to an existing wallet with a balance of", balance, "Seed phrase saved to valid_seed_phrases.txt")
        else:
            print("Seed phrase does not correspond to an existing wallet with a balance.")
    else:
        print("Invalid seed phrase")
