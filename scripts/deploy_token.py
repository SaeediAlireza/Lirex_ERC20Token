from brownie import LirexToken
from scripts.helpful_scripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(2000, "ether")


def main():
    account = get_account()
    lirex_token = LirexToken.deploy(initial_supply, {"from": account})
    token_name = lirex_token.name()
    print(lirex_token.name())
