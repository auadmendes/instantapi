FAQ about Docusign Connect and eOriginal Integration
What is Docusign Connect and how does it function?
Docusign Connect is a service that sends real-time updates (event
messages) about activities within your Docusign account to your specified
web server or application. This allows for integration with other business
systems. It provides a centralized, real-time view of transactions, can be
used for archiving documents, and helps drive reporting and workflows.
Connect sends updates about envelopes that have been sent, while
Recipient Connect focuses on updates triggered when a user on your
account is a recipient and a specific event occurs.
What types of events can Docusign Connect provide notifications for?
Docusign Connect offers a variety of event triggers to keep your systems
informed. These include Envelope events such as Envelope Created, Sent,
Delivered, Signed/Completed, Declined, Voided, Resent, Corrected, Purge,
Deleted, Discard, and Removed. Recipient events include Recipient Sent,
Auto Responded, Delivered, Signed/Completed, Declined, Authentication
Failure, Resent, Delegate, Reassign, and Finish Later. Additionally,
Connect supports events for Templates (Created, Deleted, Modified),
Docusign Click (Agreed, Declined), SMS Delivery (Opt In, Opt Out),
Maestro (Workflow Started, Failed, Completed), Identity Verification
(Pending, Completed), Extension Apps (extension-executed), and Notary
On-Demand (notary-session-completed, notary-session-terminated,
notary-session-signer-locked, notary-session-signer-unlocked,
notary-session-authentication-failed).
How can I control which users or groups trigger Connect updates?
You can configure Docusign Connect to receive event messages for all
users on an account, or for only specific users or groups. This is managed
by selecting "All Users," "Select Users/Groups to include," or "Select
Users/Groups to exclude" when creating or editing a Connect configuration.
Using group inclusion or exclusion is an efficient way to manage the flow of
Connect updates, for example, by excluding updates about a group of
users in leadership.

What are the different levels of Docusign Connect and how do they differ?
Docusign Connect is available at both the account level and the
organization level. Account-Level Connect provides updates for activities
within a specific Docusign account. Organization-Level Connect, if
available, allows you to create configurations that track activity across
multiple accounts linked to that organization. For Organization-Level
Connect, event messages are only available in JSON format and utilize the
Send Individual Messages (SIM) delivery mode. Account-Level Connect
offers more flexibility in data formats (REST v2.1 JSON or Legacy XML)
and event message delivery modes (Send Individual Messages (SIM) or
Aggregate).
How does Docusign Connect integrate with eOriginal for authoritative
document vaulting?
Docusign Connect for eOriginal facilitates the secure vaulting of
authoritative copies of completed envelopes into eOriginal. An authoritative
copy is the unique, absolute original version of an envelope. When an
envelope marked for vaulting is completed, Connect notifies eOriginal,
which then moves the authoritative copy from Docusign to its vault and
Docusign removes its original. This integration provides a compliant
vaulting solution without requiring special IT infrastructure.
How can I control which envelopes are vaulted to eOriginal?
You can control which envelopes are vaulted to eOriginal by marking them
to record an authoritative copy. This can be done in a couple of ways: by
enabling "Auto Authoritative Copy" for the entire account, which marks all
completed envelopes as authoritative copies and vaults them to eOriginal,
or by using the API to set specific envelopes or documents as authoritative
copies. If you want optional vaulting, where some envelopes are vaulted
and others are not authoritative copies (meaning they can be obtained in
Docusign), you can use the Envelope Custom Field method or provision
separate accounts for different vaulting behaviors.
What are the prerequisites for setting up Docusign Connect for eOriginal
vaulting?

Before configuring Connect for eOriginal vaulting, several prerequisites
must be met for the Docusign account. These include enabling Vaulting,
Docusign Connect, and API access with Account-Wide Rights. Optionally,
"Auto Authoritative Copy" can be enabled. You must also have an eOriginal
vault set up and ensure it's not configured to flatten files from Docusign.
The integrating user for eOriginal also requires specific permissions in
Docusign, such as "Account-wide access" and "Can export authoritative
copy?".
What are the prerequisites for using Recipient Connect and how do
authentication settings affect document inclusion in messages?
To use Recipient Connect, your production account must have it enabled
(it's enabled by default for developer accounts). Messages from Recipient
Connect are only available in JSON format. Crucially, updates are only
triggered by "qualified recipients," which are recipients with an email
address in a claimed domain and whose primary account has a Recipient
Connect configuration. For a recipient to trigger an update, their account
must be linked to the organization that claimed their email domain and
have a Recipient Connect configuration.
Regarding document inclusion in Recipient Connect messages, whether or
not the envelope documents are included depends on the sender's
recipient authentication settings. If the qualified recipient is not required to
authenticate, you always receive the documents. If the qualified recipient
must authenticate every time they access the envelope, you never receive
the documents. If the qualified recipient must authenticate only the first time
they access the envelope, you receive the documents after they complete
their role (e.g., signing). Specific legacy authentication settings also
influence document inclusion based on whether authentication is required
and how frequently.

Here are 20 questions and answers based on the provided source material
about Docusign Connect:

What is Docusign Connect? Docusign Connect sends updates (event
messages or webhooks) about your Docusign activity to other applications.
It allows you to choose the events that you want to follow. Your application
can receive event messages for various actions, such as when an
envelope is re-sent or corrected, a recipient reassigns an envelope, or a
template is created. Connect sends these event messages in JSON or
XML format through HTTP POST requests.
How does Docusign Connect work? Connect works by monitoring
Docusign workflows for specific event triggers. When an event you are
following occurs, Connect sends a notification message. This message is
received and processed by your application's listener. The overall flow
involves your users taking an action, Docusign processing the action and
advancing the workflow, Connect monitoring for triggers and sending a
notification, and your listener receiving and processing the message.
What are some common use cases for Docusign Connect? Docusign
Connect messages can be used to kick off downstream actions in your own
systems. Examples include downloading data like a sales order ID from an
envelope custom field to start the next step in a sales process. You can
also use Connect to archive documents, get a centralized, real-time view of
transactions for users on your account, and drive reporting or workflows for
your organization.
What are the prerequisites for using custom Docusign Connect
configurations? To use Connect for custom configurations, you should have
development resources. You must also create a webhook listener. Setting
up groups beforehand is necessary if you want to follow only selected
groups of users.
What are the URL and security requirements for a Docusign Connect
webhook listener? The URL for your listener must use the HTTPS protocol
and SSL/TLS connections. It may include query parameters. By default,
Connect uses port 443 for HTTPS, but you can specify alternate ports like
1443, 2443, 3443, 4443, 5443, 6443, 7443, 8443, or 9443 in the URL. The
SSL and TLS certificates for your web server must chain to a Certificate
Authority (CA) in Microsoft’s list of trusted CAs. Self-signed certificates do
not work. You may use free certificates from Let’s Encrypt.

What security methods does Docusign Connect offer besides X.
certificates? Besides X.509 certificates, Docusign also offers HMAC and
OAuth as security methods. These methods are described as easier to set
up. You can also enable Basic Authentication for Account-Level Connect
messages, and add Mutual TLS authentication and authorization to a
configuration. Connect does not support using OAuth with Basic
Authentication.
What is Recipient Connect and how does it differ from standard
Connect? Recipient Connect sends updates about inbound envelopes to
other applications. Updates trigger when an account user is a recipient and
a specific envelope or recipient event occurs. Unlike standard Connect,
which sends updates about sent envelopes, Recipient Connect updates
trigger based on events related to envelopes received by a user on your
account. Your application receiving the update does not need association
with or permissions from the sender.
What are the prerequisites for using Recipient Connect? The
prerequisites for using Recipient Connect include a webhook listener, a
production account with Recipient Connect enabled, a Docusign
organization, one or more claimed domains associated with the
organization, and the organization must be linked to the accounts that will
receive envelopes and trigger Recipient Connect. Organizations using
Recipient Connect may claim a domain for free. Recipient Connect is
enabled by default for developer accounts but requires contacting your
Docusign account team for production accounts.
What data formats does Docusign Connect use, and what format does
Recipient Connect use? Standard Docusign Connect sends event
messages in JSON or XML format. For Account-Level Connect, the
available events depend on the chosen Data Format and Event Message
Delivery Mode. However, Organization-Level Connect configurations
support event messages only in JSON format. Recipient Connect only
sends messages in JSON format. The Data Format field is unavailable for
Recipient Connect configurations because REST v2.1 is always the format.
What types of events can Docusign Connect follow? Connect allows
you to follow various events related to your Docusign activity. These include
Envelope events (e.g., Created, Sent, Delivered, Signed/Completed,
Declined, Voided, Resent, Corrected, Purge, Deleted, Discard, Removed),
Recipient events (e.g., Sent, Auto Responded, Delivered,
Signed/Completed, Declined, Authentication Failure, Resent, Delegate,
Reassign, Finish Later), Template events (e.g., Created, Deleted,
Modified), Docusign Click events (e.g., Click Agreed, Click Declined), SMS
Delivery events (e.g., SMS Opt In, SMS Opt Out), Maestro events (e.g.,
Workflow Started, Failed, Completed), Identity Verification events (e.g.,
Pending, Completed), Extension Apps events (e.g., extension-executed),
and Notary On-Demand events (e.g., notary-session-completed,
terminated, signer-locked, signer-unlocked, authentication-failed).
What additional data can be included in Connect messages using the
REST v2.1 (JSON) format? When receiving messages in the REST v2.
(JSON) format, you can choose to include additional data such as Custom
Fields, Documents, Attachments, Extensions (reserved for Docusign),
Folders, PowerForm, Prefill Tabs, Document Fields, Recipients, Payment
Tabs (if Recipients is selected), and Tabs (if Recipients is selected).
Templates can also be included.
How can documents be included in standard Connect messages? You
can set up Connect messages to include envelope documents in PDF
format. This is configured in the Docusign web application. When setting up
a Connect configuration, under Trigger Events, in the Envelope and
Recipients section, you select Include Data and then select the checkbox
for Documents.
What is the recommended alternative method for retrieving documents
instead of including them in Connect messages? If throttling of document
retrieval, file size, and storage are concerns for your architecture, it is
recommended to retrieve the documents using API requests after receiving
the Connect event message. This approach can help prevent your
processing routines from being overwhelmed by high volume or spikes and
allows you to throttle file processing at a time that makes sense for your
workflow. Connect sends PDF documents in Base64-encoded format,
which is about a third larger than binary format, potentially impacting
storage.

What happens if your Docusign Connect listener does not acknowledge
a message? When the Require Acknowledgment option is enabled for a
configuration (which is automatically enabled for Organization-Level
Connect and selected by default for Account-Level Connect), Connect
waits for your listener to return an HTTP 200 - OK status code within 100
seconds. If this code is not returned, Connect records a failure. Failed
transmissions are then eligible for manual or automated retries. If Require
Acknowledgment is not selected, your listener might not receive status
information, and Connect typically does not retry failures.
How does Docusign handle failing Connect configurations? Connect
configurations that are no longer reachable automatically deactivate. This
prevents failing endpoints from blocking message delivery. If a
configuration fails nearly every time over three days, its status changes to
Active - Pending Deactivation. After a total of at least 14 days, the status
becomes System Deactivated. Deactivation stops new messages to the
endpoint but does not affect API access. Administrators are notified by
email when a failing configuration is scheduled for deactivation.
How are Docusign Connect message failures retried? Connect
automatically retries failed message deliveries for Organization-Level
Connect configurations and Account-Level configurations with the Require
Acknowledgment option selected. Retries use exponential back-off. The
sequence of retries is 5 minutes, 10 minutes, 20 minutes, 40 minutes, 1
hour, 2 hours later, and then once per day for a 15-day span.
What are the configuration limits for Docusign Connect? There are
limits on the number of Connect configurations you can add to an account.
These limits include: 40 total Organization-Level Connect configurations
(with 20 total active), 20 Connect Custom/Custom Recipient configurations,
20 Connect for Box configurations, 20 Connect for OneDrive
configurations, 1 Connect for eOriginal configuration, and 1 Connect for
Salesforce configuration.
What is Organization-Level Connect (OLC) and what benefits does it
offer compared to Account-Level Connect (ALC)? Organization-Level
Connect (OLC) is an enterprise feature that offers a single view of all your
Connect configurations across multiple accounts. It provides enhanced
filtering and allows for creating OLC configurations that track activity across
accounts. Benefits include centralized management, streamlined
operations, improved compliance, enhanced productivity, managing
security settings across accounts, quickly identifying failing configurations,
and receiving specific notifications like certificate expiration warnings. ALC
is included with paid Docusign plans and is suitable for smaller
organizations or those with fewer accounts. OLC configurations only
support JSON/SIM format and HMAC, TLS, and OAuth security methods,
not Basic Authentication, while ALC supports XML/Aggregate and Basic
Authentication options.

What is Docusign Connect for eOriginal and how does it work?
Docusign Connect for eOriginal vaults authoritative copies of completed
envelopes to eOriginal. An authoritative copy is the single, distinct, absolute
original version of an envelope. When an envelope that needs to be vaulted
is completed, Connect notifies eOriginal. eOriginal then uses API calls to
move the authoritative copy from Docusign to eOriginal, and Docusign
removes the original envelope from its system. eOriginal then manages the
authoritative copy. It does not require special IT infrastructure and works
with existing business systems.
How does sender authentication affect whether documents are included
in Recipient Connect messages? Even if you select the option to include
documents in a Recipient Connect configuration, the messages will only
include the documents if the sender uses certain recipient authentication
settings.
If the qualified recipient does not have to authenticate, you always receive
the documents.

If the qualified recipient must authenticate every time they access the
envelope, you never receive the documents.

If the qualified recipient must authenticate the first time they access the
envelope, you receive the documents when the recipient completes their
role. If the sender uses Legacy Authentication and "Disable recipient

authentication for this account" is selected, messages always include the
documents. Senders can configure their authentication settings, either
Legacy or Identity Verification, to allow the receiving organization to get
documents with messages.