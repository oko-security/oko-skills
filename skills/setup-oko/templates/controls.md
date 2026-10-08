# Standard controls

Controls every service inherits unless its threat model says otherwise.
Threat rows cite these by name in `controls`.

| name | covers | evidence | notes |
|---|---|---|---|
| sso-oidc | Spoofing of workforce users on internal apps | <link to policy/IaC> | |
| edge-waf | Common web attacks on public HTTP | <link> | Not a substitute for parameterized queries |
| mesh-mtls | Service-to-service spoofing/tampering in cluster | <link> | |
| secrets-manager | Secret disclosure from source/config | <link> | |
