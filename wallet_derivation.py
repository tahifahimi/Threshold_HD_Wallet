from bip32 import BIP32
from sslib import shamir
from mnemonic import Mnemonic

def convert_shares(shares: dict):
    result = []
    for s in shares['shares']:
        result.append(s[1])
    return result

def dealer(mnemonic: str):
    # Generate a random BIP32 master key
    mnemonic_bytes = Mnemonic.to_seed(mnemonic= mnemonic)
    master_key = BIP32.from_seed(mnemonic_bytes)

    # (2,3) system
    shares = shamir.split_secret(master_key.get_xpriv_bytes(), 2, 3)
    print(convert_shares(shares))
    """send the result of conver_shares to the users"""
    # if shamir.recover_secret(shares) == master_key.get_xpriv_bytes():
    #     print("ok")



seed_phrase = "letter advice cage absurd amount doctor acoustic avoid letter advice cage above"
dealer(seed_phrase)