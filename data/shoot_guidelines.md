# SHOOT Package Guidelines – Live Application URL

- **Every SHOOT package must include an `Application URL` field in the **HEADER** section** that points to the exact live job posting URL (e.g., Greenhouse, Oracle Cloud, Lever, Workday, etc.).
- The URL should be the one you actually used to access the posting – not a generic company careers homepage.
- If the job was found via a search engine or aggregator, capture the final redirected URL after any tracking parameters are stripped.
- Include the URL in a markdown table as follows:
  ```
  | **Application URL** | <live URL>
  ```
- The URL is used by the system for:
  * Automatic link generation in the networking cadence footer.
  * Quick navigation when you run `FETCH` or `SHOOT` commands.
  * Auditing that the job is still live before you submit.
- When you create a new SHOOT package (manually or via a future generator), **add the URL** before committing the file.

*This rule is now part of the permanent kernel and will be enforced for all future SHOT packages.*