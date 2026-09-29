# Security and candidate privacy

Use synthetic data when reporting a problem. Do not post resumes, compensation, recruiter messages, access tokens, authentication cookies, or application HTML containing personal fields in public issues.

If the repository's GitHub Security tab offers **Report a vulnerability**, use it for a private report. Otherwise open a minimal issue requesting a private reporting channel without disclosing exploit details or personal data. No private reporting service is configured by these files alone.

Include the affected skill or script, a minimal redacted reproduction, the observed effect, and the revision tested. Problems such as unintended file replacement, executing instructions embedded in supplied HTML, or disclosing candidate information are relevant reports.

RoleCraft distributes local instructions and helper scripts. Data access, web requests, and external actions are performed through the chosen agent and its tools under that host's permissions. Review the applicable skill before use. Git ignore rules reduce accidental additions but cannot prevent a user or tool from publishing data from another path.

Security fixes are developed against the current main branch; this project does not promise maintenance of older snapshots.
