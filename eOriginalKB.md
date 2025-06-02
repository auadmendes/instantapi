You can improve the
accuracy of search results by including phrases that your customers use to
describe this issue or topic.xeOriginal Troubleshooting, eOriginal
configuration, eOriginal queries, eOriginal how-to, optional vaulting
troubleshooting

Article Type

External URLN/A

Internal
URLhttps://docusign.lightning.force.com/lightning/articles/Knowledge/eOrigi
nal-Troubleshooting

SolutionHelp SolutionDescription of the solution to resolve the stated issue
or errorTable of Contents
How does eOriginal work with Docusign?
BasicsEnvelope flow with eOriginal
What are common errors seen with the integration?EnvironmentsGeneral
configuration steps
DocusignDocusign permissions neededeOriginal
Queries to confirm functionalityOptional Vaulting
Envelopes not being set as Authoritative CopyEnvelopes unintentionally
vaulting with eOriginalRepublishing envelopes with "Vault with eOriginal"
set to "No"

How does eOriginal work with Docusign?
Basics
eOriginal is a partner of Docusign
https://partners.docusign.com/s/partner-solution/aNR1W000000PAuO/docu
sign-asset-vaulting-by-eoriginal-for-docusign-esignature
eOriginal manages eAssets:
https://www.wolterskluwer.com/en/solutions/eoriginal/asset-managementeO
riginal will vault Docusign envelopes based on Envelope Complete events

In general, eOriginal is used to vault envelopes and documents that are
marked as Authoritative CopyBased on the eOriginal configuration,
non-Authoritative Copy envelopes can also be vaulted

Envelope flow with eOriginal
On the Envelope Complete eventDocusign Connect sends a payload to the
eOriginal webhook listener (see below)Based on this event, eOriginal
makes a sequence of SOAP API callsThese API calls flow as follows
(which you'll see in logs):
RequestEnvelopeV2ExportAuthoritativeCopyGetAuthoritativeCopyExportK
eyRequestCertificateCompleteAuthoritativeCopyExport

What are common errors seen with the integration?
Authoritative Copy Export Error: Envelope not authoritative copy.
Envelope was not created as Authoritative Copy and eOriginal will not vault
envelopeSee this page on how to set Authoritative Copy status in an API
callIf using the web app only, the account needs to have the Auto
Authoritative Copy setting enabled in IAC
Authoritative Copy Export Error: This User lacks sufficient permissions
The user profile used to authenticate the Docusign/eOriginal integration
needs to have the "Can export Authoritative Copy" setting enabled in IAC
Envelope has only partially vaulted to eOriginal while the whole envelope
was marked as Authoritative Copy in Docusign
This is due to an issue with the eOriginal API calls; eOriginal is
investigating a potential fix for this concern; reports of this should go to
eOriginal Support (support@eoriginal.com)
Envelope Custom Field (ECF) values not syncing to a vaulted envelope's
record in eOriginal
When the Connect event (Envelope Complete) fires to eOriginal's
webhook, we include metadata in the XML payload which includes a
......</Custo
mField> objectThis data should include ECF valuesYou
can find any successes or failures for these payloads from the
ConnectEvents table (see First Step sub-section/query from the "Queries to
confirm functionality" section below)If you cannot see anything amiss here,

it may be necessary to review Connect logs with the customer to see if
there are missing values in the Connect payload, errors in the Connect
Logs, etc.
Envelopes are not vaulting and during troubleshooting you find that
Connect is returning the following error:
https://ondemand.eoriginal.com/docusign-listener/ :: Error - WSE101: An
asynchronous operation raised an exception.; WSE805: An HTTP
response was received that used the following unsupported
ContentTypeThis error message means that there is a configuration issue
in eOriginal and that you will need to refer the customer to them to delete
and reconfigure.
Login difficulties when you attempt to reconnect eOriginal to your Docusign
account.
Make sure to enter the App Password that you’ve generated into the
Docusign Password field, not your regular user-login password.

Environments
Production: https://ondemand.eoriginal.com/docusign-listener/Preview
(pre-production):
https://previewondemand.eoriginal.com/docusign-listener/Test (initial
testing and setup): https://testondemand.eoriginal.com/docusign-listener/
General configuration steps
General steps here:
https://support.docusign.com/en/guides/ndse-admin-guide-connect-for-eori
ginal
Docusign
Connect needs to be enabledSet up and activate the vaulting user needs
on the account. There are two ways to go about this:
Vaulting user can be granted DS Admin permissionsVaulting user can be
granted heightened permissions
Admin Permissions
None
User Permissions
Allow view and manage envelope rights through API**There is a potential
that, during initial setup, the vaulting user will need the DS Admin (full

permissions) role to verify the integration is working. If needed, the vaulting
user can be moved to only include the aforementioned user permissions.
This "lower" permission option is for those clients that are worried about
granting the DS Admin role to an integration user.

In Docusign, go to Settings > Integrations > Connect > Add Configuration >
eOriginal
Status: ActiveEnvironment: pick applicable environmentEnable Log
(recommended that this is enabled)Add associated usersSave
configuration
In IAC (Internal Admin Console), find the account and find the Auto
Authoritative Copy setting > enable > save configuration In IAC (Internal
Admin Console), find the user whose credentials will be used for vaulting >
go to View Membership > Permissions
Enable the "Can Export Authoritative Copies?" setting > save permissions
for this user

eOriginal
Log into the correct eOriginal environment (EOD, POD, TOD)Go to
Preferences > Partner Configuration > Docusign ConnectAdd Account
You will be prompted to add the user credentials whose profile will be used
to vault.
Note: You’ll need to enter the App Password that you’ve previously
generated into the Docusign Password field.
eOriginal will validate the credentials against the environment and account
ID (nice ID, not GUID)Once credentials are validated, you will be redirected
to the full configuration page with the options to sync Envelope Custom
Fields, and other base fields
Example configuration page:
Save settingsSend a test envelopeReview envelopes's history to ensure
proper settings and permissions are in place
Failed Export

Successful export

Queries to confirm functionality
First Step: Docusign Connect Sends payload to eOriginal
ConnectEvents
| where Timestamp between (datetime(2021-10-11T00:00:00Z) ..
datetime(2021-10-11T23:23:59Z))
and EnvelopeId =~ "ENVELOPE_GUID"
// UNCOMMENT CORRECT ENVIRONMENT AND COMMENT OUT THE
OTHER TWO
and ConnectListenerURL =~
"https://ondemand.eoriginal.com/docusign-listener/" // aka PROD
// and ConnectListenerURL =~
"https://previewondemand.eoriginal.com/docusign-listener/" // aka POD
// and ConnectListenerURL =~
"https://testondemand.eoriginal.com/docusign-listener/" // aka TOD
and IntegrationType =~ "eOriginal"
| limit 100
| order by Timestamp desc
Second Step: eOriginal makes SOAP requests to Docusign to vault
Authoritative Copy
RequestEvents
| where Timestamp between (datetime(2021-10-11T00:00:00Z) ..
datetime(2021-10-11T23:23:59Z))
| where Application =~ "API3-0"
| where AccountId =~ "ACCOUNT_GUID"
| where EnvelopeId =~ "ENVELOPE_GUID"
| where IntegratorKey has "EORI"
// specific eO SOAP API calls
and Action in (
"RequestEnvelopeV2",
"ExportAuthoritativeCopy",

"GetAuthoritativeCopyExportKey",
"RequestCertificate",
"CompleteAuthoritativeCopyExport"
)
| limit 100
| order by Timestamp desc
| project Timestamp, TraceToken, AccountId, EnvelopeId, Application,
HTTP_RESPONSE_STATUS_CODE, HTTP_X_FORWARDED_FOR,
REQUEST_METHOD, Action, EnvelopeStatus, EnvelopeStatusChange,
ErrorLog=iff(ErrorCode != "", ErrorCode, tostring(0))
Optional Vaulting
Envelopes not being set as Authoritative Copy
As stated in previously, the envelopes or their documents need to be set as
Authoritative Copy to be available for vaulting. This can be done in 2 ways:
Setting the account with Auto Authoritative Copy, making ALL envelopes
sent by the account Authoritative Copies upon completion.Using API to set
specific envelopes or documents as Authoritative Copies. More information
on how to do this can be found here.
Check with customer which options they intend to be using. If their intention
is to use the Envelope Customer Field method, then make sure that Auto
Authoritative Copy is enabled for the account.
Envelopes unintentionally vaulting with eOriginal
The process to set an Envelope Custom Field in the envelopes sent by the
account to mark which ones will be vaulted by which ones will not is
described in the following article:Setup eOriginal vaulting as optional on
envelopes with custom fieldsThe processing of the Vault with eOriginal ECF
is done in the eOriginal side, so Connect will send information to them
regardless of its value. If the envelope is being vaulted when the intention
is not to vault it, 2 conditions need to be confirmed to ensure that there are
no extra spaces or incorrectly capitalized letters.
The ECF is named “Vault with eOriginal” exactly. The value in the field
needs to be set as “No”.

Republishing envelopes with "Vault with eOriginal" set to "No"

If the customer has set envelopes that were supposed to be vaulted but
had the “Vault with eOriginal” customer field set to “No” (see previous topic
for more info), republishing them will not be enough to vault them as the
ECF will still be sent to eOriginal. As it cannot be changed in Docusign, the
customer will have to contact eOriginal’s support team to check if it's
possible to disregard the the “Vault with eOriginal” customer field on their
side once the envelope is republished.

SummaryHelp SummaryBriefly describe the article. The summary is used
in search results to help users find relevant articles. You can improve the
accuracy of search results by including phrases that your customers use to
describe this issue or topic.eOriginal onboarding enablement
stepsConfigure eOriginal integrationeOriginal with Docusign

Article Type

External URLN/A

Internal
URLhttps://docusign.lightning.force.com/lightning/articles/Knowledge/eOrigi
nal-Enablement-Steps

SolutionHelp SolutionDescription of the solution to resolve the stated issue
or errorTable of Contents
SummaryRequired Account SettingseOriginal Customer Onboarding
FlowIntegrator User as DS Admin or custom permission
profileTest/validation steps from the eOriginal side of the
configurationResources
Summary
An authoritative copy is the single, distinct, absolute original version of a
document that is unique, identifiable, and unalterable without detection. You
can specify whether all the documents in an envelope are authoritative
copies or just specific documents.
After an agreement, authoritative copies are watermarked, then vaulted
and stored in an external system such as eOrginal.

eOriginal is sold using the following SKUs:
eOriginal Asset ManagementeOriginal eAsset Transactions
The module 2016 - eOriginal and Authoritative Copy is enabled in the
Internal Admin Console once the order has processed.

Vaulting/Authoritative Copy features are included in the following plan
types:
Enterprise Pro Enterprise Pro for Salesforce Financial Services Pro
If the customer is requesting that vaulting/eOriginal be enabled for one of
the above plans, (per PnP) these features can be enabled by anyone in
Support as they are in plan.
If the customer is requesting vaulting/eOriginal, and the module: “2016 -
eOriginal and Authoritative Copy”, is not listed on the account in Internal
Admin Console (IAC), please reassign the case to the Account Services
Team (AST). AST will review the order form and reach out to the
customer’s Account Team for an upsell.
Backend account settings and user permissions are required in IAC in
order for the eOriginal integration to work. These settings/permissions allow
for the following:
The account to generate Authoritative Copy envelopes automaticallyThe
integrator/vaulting user for eOriginal to successfully export Authoritative
Copy documents
This requires authenticated API calls from eOriginal to Docusign to be
made with a particular set of permissions.

Vaulting can be setup in one of the following ways:
Main Account is Auto Authoritative Copy: All envelopes sent from the
account are marked as Authoritative Copy.Sub-Account is Auto
Authoritative Copy: If the customer does not want the main account to have
Auth Authoritative Copy enabled, a sub-account can be provisioned for
vaulting purposes. API-first Authoritative Copy: some accounts do not want
all envelopes to be marked as Authoritative Copy and can define envelopes
in an ad hoc basis via the API.If the account is API-first AC, admins must
verify the correct user permissions are enabled for the vaulting

user.Envelopes are marked as AC via API call payload. The account-level
Auto Authoritative Copy setting does not need to be enabled

Required Account Settings
Backend account settings and user permissions are required in IAC in
order for the eOriginal integration to work. These settings/permissions allow
for the following:
The account to generate Authoritative Copy envelopes automatically.The
integrator/vaulting user for eOriginal to successfully export Authoritative
Copy documents.This requires authenticated API calls from eOriginal to
Docusign to be made with a particular set of permissions.
Auto Authoritative Copy (AC): account-wide setting makes all envelopes
created after the setting is enabled to be flagged as Authoritative Copy
(AC). If Automatic AC is not wanted, customers can either have a separate
sub-account specifically for Automatic AC envelopes, and/or create AC
envelopes via the API on an ad hoc basis.Integrator User/Vaulting User:
refers to the user whose credentials are used to authenticate API calls from
eOriginal to Docusign
Required account settings in IAC:
Connect: AllowedAuto Authoritative Copy: EnabledEnvelope Custom
Fields: EnabledAllow Fax Delivery to recipients: DisabledAllow signing on
paper: Disabled

Required integration/vaulting user settings.
These settings are found in IAC under the specific user’s Permission
Profile.
Can export Authoritative Copy?: EnabledAccount-wide access: Enabled
eSign Admin's have his permission by default.
This can also be set by an eSign admin in the Permission Profile via the
Docusign WebApp. Permission Profile in Docusign Web
App:Administrative Access tab: None.
User Permissions tab: Allow view and manage envelope rights through
API: Enabled

eOriginal Customer Onboarding Flow
eOriginal completes testing in their Sandbox, then moves to a production
vault after testing passes for customer.The current-state (demo or
production) Docusign accounts sometimes do not have proper account
and/or user permissions set, with which Docusign must assist.
See steps above.

Integrator User as DS Admin or custom permission profile
The Integration user is only required to have “Account-wide access” and
“Can export authoritative copy?” user permissions.There can be issues with
the initial configuration if the user is NOT initially set to DS Admin. The
customer must determine if they want the integration user to be an eSign
admin, or if they want to create a custom permission set in their Docusign
WebApp.

Test/validation steps from the eOriginal side of the configuration
Checking for Envelope History/test envelope
Envelope history shows the following when it is completed and flagged as
Authoritative Copy:

Validate with DS Support
Support can check if Auto Authoritative Copy is enabled at account
levelSupport can check if the integrating user has Account-wide Access
and Can Export Authoritative Copy?
Account-level audit log

.Learn how to set up eOriginal for Docusign via several different methods
as the account administrator.

Article Type

External
URLhttps://support.docusign.com/s/articles/optional-eOriginal?language=e
n_US

Internal
URLhttps://docusign.lightning.force.com/lightning/articles/Knowledge/option
al-eOriginal

SolutionHelp SolutionDescription of the solution to resolve the stated issue
or errorYou can control which Docusign envelopes are vaulted to eOriginal
through a few different methods. This article covers using the Envelope
Custom Field method.

Important: Using this method does not make the envelopes that are set
with "Vault with eOriginal" as "No" to not be Authoritative Copies. All
envelopes in an account with Auto Authoritative Copy enabled are
Authoritative Copy, meaning they cannot be obtained in Docusign and must
be sent to a service like eOriginal. If you want to have some envelopes go
to eOriginal and others that are not Authoritative Copies, you must take one
of the following two actions:

Employ user API to determine the envelopes that should be Authoritative
Copies.

OR
Ask your account team to create another account. This should include one
that sends all envelopes to eOriginal (Auto Authoritative Copy = enabled)
and another that keeps the documents in DocuSign (Auto Authoritative
Copy = disabled).

If you want to determine which envelopes in an account with Auto
Authoritative Copy enabled should be stored in eOriginal, and which should
be kept as an Authoritative Copy to be sent to another service, follow the
steps below in this article.
Steps
Prerequisites: Setup your account to vault with eOriginal
Have a Docusign Administrator select the Admin tab from the top banner
across the main Docusign page and select Envelope Custom Fields

Select Add Field to create a new one Field Name = Vault With
eOriginal.Show field to envelope creators = Checked, otherwise users
won't see it.Make field required for envelopes = Checked, based on
preference.Field Type = List.List of Values = Yes;No.

Select Add to finishStart a new envelope draft and set it up however you
like; you should see a Document Labels header with a Vault With eOriginal
dropdown menu below Add Recipients. If you want to vault the envelope,
select Yes and vice versa; send the envelope and once it is completed, it
will vault or not depending on what you selected on your Document Label.
With this setup, envelopes that are not vaulted are still moved to
Authoritative Copy. The remainder of this configuration is setup with
eOriginal.

Comments (Internal Only)Note: This workflow relies on the DocuSign
Connect for eOriginal config to pass the Envelope Custom Field label and
value to eOriginal.