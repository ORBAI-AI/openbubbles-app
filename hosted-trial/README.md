# ORB hosted iMessage trial

This fork is the starting point for a hosted iMessage integration. It does not
yet contain a hosted worker or an Apple login web interface. No live messaging
trial has been qualified.

## Public-source prerequisite check

Run `python3 hosted-trial/source_preflight.py` after initializing submodules.
Exit 2 indicates missing source prerequisites. Exit 0 is not an Apple activation,
authentication, send, receive or synchronization qualification.

Inspected upstream application revision: `eed1b6332efbb17adbf5ebfa2263ad770169f75e`.
Pinned rustpush revision: `a7fab473e7a33325a760635285db2860de8e1cb0`.

The public Mac validation dependency, OpenAbsinthe-Stub, explicitly identifies
itself as a nonfunctional placeholder. Its `ValidationCtx` methods contain
`todo!()`. Hardware data exported by Mac-Hardware-Info supplies identifiers;
it does not replace that validation implementation.

Rustpush's activation source includes signing material absent from the public
checkout. The upstream application CI substitutes legacy/sample material for
development builds. Such a build is not evidence of successful activation.
Do not manufacture replacements, publish keys, or label a mock as connected.

## Execution path still required

The direct engine path needs an executable validation implementation and valid
activation prerequisites, or a supported managed activation provider. The
engine also has a relay configuration path; it requires an actual provisioned
Apple device and running validation service. No relay is provisioned by this
fork, and no third-party credentials embedded in upstream code are reused.

After that prerequisite is resolved, a hosted worker must own the Apple session,
encrypted state, persistent push connection, reconnect and registration renewal.
Login and 2FA must pass through a secure user interface. Real sends, incoming
messages, history, cross-device unread state, sender identity, worker restart,
revocation and account isolation require live qualification before enabling the
integration. Users should not need to keep their own Mac running.

The application and dependency licenses differ. Public customer hosting requires
review of the applicable dependency and activation-runtime rights. This source
inspection does not establish those rights or require vendor email before
prototype development.
