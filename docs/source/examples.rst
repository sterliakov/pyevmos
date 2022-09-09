Examples
========

In this examples we'll broadcast a transaction for sending some funds to another address.

Sending with keplr-style transaction
------------------------------------

.. code-block::

    from evmos.transactions import Sender, create_message_send
    from evmos.wallet import (
        TESTNET_CHAIN,
        TESTNET_FEE,
        broadcast,
        sign_transaction,
    )

    url='https://rest.bd.evmos.dev:1317'  # REST API url (here for testnet)
    sender_pk='...'  # Private key (hex, without 0x prefix)
    receiver_addr='evmos1...'  # Receiver address, bech32

    sender = Sender(
        account_address='evmos1...',  # Actual sender address
        # base64 encoded public key, if it is first tx for this address,
        # may be omitted otherwise
        pubkey='A1...',
    )

    sender.update_from_chain(url)  # Fetch nonce, account number and pubkey, if known

    tx = create_message_send(
        TESTNET_CHAIN,
        sender,
        TESTNET_FEE,
        '',
        receiver_addr,
        '1',
        'atevmos',
    )

    signed = sign_transaction(tx, sender_pk)
    response = broadcast(signed, url)

    assert response['tx_response']['code'] == 0


Sending with EIP-712 transaction
--------------------------------

.. code-block::

    from evmos.transactions import Sender, create_message_send
    from evmos.wallet import (
        TESTNET_CHAIN,
        TESTNET_FEE,
        broadcast,
        sign_transaction_eip712,
    )

    url='https://rest.bd.evmos.dev:1317'  # REST API url (here for testnet)
    sender_pk='...'  # Private key (hex, without 0x prefix)
    receiver_addr='evmos1...'  # Receiver address, bech32

    sender = Sender(
        account_address='evmos1...',  # Actual sender address
        # base64 encoded public key, if it is first tx for this address,
        # may be omitted otherwise
        pubkey='A1...',
    )

    sender.update_from_chain(url)  # Fetch nonce, account number and pubkey, if known

    tx = create_message_send(
        TESTNET_CHAIN,
        sender,
        TESTNET_FEE,
        '',
        receiver_addr,
        '1',
        'atevmos',
    )

    signed = sign_transaction_eip712(sender, tx, sender_pk)
    response = broadcast(signed, url)

    assert response['tx_response']['code'] == 0
