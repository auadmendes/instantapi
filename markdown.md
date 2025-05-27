AATL = adobe approved trust list

EUTL= European Union trust list

EUTL will indeed be for QES, to be a QES signature, the certificate authority has to be in the
EUTL

AATL is not tied to any regulation, it's just what adobe approves

TSP = Trust Service Providers
3:

Internal
URLhttps://docusign.lightning.force.com/lightning/articles/Knowledge/Trusted-Service-Provider-
FAQ

SolutionHelp SolutionDescription of the solution to resolve the stated issue or errorDocusign
Trust Service Provider FAQs
What is a Trust Service Provider (TSP)?TSP stands for Trust Service Provider. As per eIDAS, a
TSP is a provider who delivers a “trust service” - in the case of our Standards-Based Signature
offering, a digital signature associated with the issuance of a digital certificate. In the context of
our SBS suite, there are two flavors of TSPs:
Docusign France: Docusign acts as a TSP for Express and EU AdvancedA third party that is
integrated through our TSP API in our signing experience, in order to enable a signer to perform
a digital signature with a specific credential
What is the Trust Servide Provider Program?The TSP Partner Program is part of the global
Docusign partner effort. It brings companies that specialize in electronic ID and trust services
into a European ecosystem to provide the full range of eIDAS-defined signature types through
the Docusign platformWhat to do if a customer is looking for pricing information?Customers
should be redirected to their Account Team for pricing information or advised to create a case in
Docusign Support Center. However, note that using a TSP requires both direct buy from the
TSP and a setup in Docusign. How to see if a TSP is setup on a Docusign account?Customer
Support should not setup a TSP on a customer account. However, for a TSP configuration to
work, Standard-based Signatures (in the Account Plan Editor must) be enabled on an account,
and the Universal Signature Settings must be configured. See Standards-Based Signatures
Internal Admin Guide for additional information.Do TSPs work with the Classic Docusign
Experience?No, envelopes utilizing a TSP should be sent from the New Docusign Experience or
the API. Also, oldest signing versions (v0, v1) are not supported during signing.How do I know it
is a TSP being used?

Details are captured in the Envelope History action: "Redirected to Signing Provider". The URL
will indicate which Trusted Service provider ( TSP) was used.During Signing the modal window
will help indicate which TSP is being used

TSPSigning ScreenshotItAgile IdNow SwisscomBankID
Who can I contact when having an issue with a TSP?Please check with Tier 3 prior to
contacting one of the TSPs listed below. Tier 3 will then advise if the TSPs can be contacted.For
questions about the TSP Program, you can reach folks involved at Docusign with Help for Trust
Service Providers TSP Program TSPhelp@docusign.com

TSP NameCountries/LanguagesSupport ContactOperations/DevOps/Engineering Contact
IDnow

https://www.idnow.eu/
DE, ES
+49 89 2488 92820

support@mail.idnow.de

https://www.idnow.eu/contact

https://support.idnow.de/

Escalation path:

Andreas Kofer (Head of Engineering)
andreas.kofer@idnow.deArmin Bauer (Managing Director & Co-Founder)
armin.bauer@idnow.de

itAgile

http://www.itagile.it/docusign/
IT
https://assistenza.itagile.it/

Customer code: Docusign Password: 32he89a

Emergency 24x7 contact: +39 06 94801505 (Italian operator)

Escalation path:

Gianni Sandrucci (CEO)
gianni.sandrucci@itagile.it

Swisscom
CH

Additional Resources

Standards-Based Signatures FAQsChatter
TSP PartnerStandard-Based SignaturesWhat’s available now
Confluence
TSP Partner Program TSP - Support and DOC InfoSBS Products
Help Aliases
Help for Trust Service Providers TSP Program - TSPhelp@docusign.comHelp for
Standards-Based Signatures - SBShelp@docusign.com

Internal
URLhttps://docusign.lightning.force.com/lightning/articles/Knowledge/DocuSign-Standards-Base
d-Signatures-FAQs

SolutionHelp SolutionDescription of the solution to resolve the stated issue or errorDocusign
Standards-Based Signatures FAQs
What is Docusign Standards-Based Signatures?Docusign Standards-Based Signatures is a
core feature of Docusign’s platform that enables customers to enjoy the full range of Docusign
Signature capabilities while staying compliant with local and industry e-signature standards.
Similar to carrier-grade availability, Docusign Standards-Based Signatures is a platform feature
that is available across all of Docusign’s applications and integrations. In the EU, there are
three key signatures in the Docusign Standards-Based Signature portfolio, Express Signature,
EU Advanced Signature and EU Qualified Signature. EU Qualified Signature is required for only
a small minority of EU legally regulated use cases. Over time there will be an increasing number
of signature options available in the Standards-Based Signature portfolio, including offerings
provided by partners through our Trust Services Provider (TSP) partner program. How are
digital signatures related to Standards-Based Signatures? Docusign has supported digital
signature technology since 2013. Digital signatures use PKI, a broadly accepted technology
standard that incorporates encryption technology as part of the signing process. In regions such
as continental Europe, Latin America, and Asia, digital signature technology is often the
preferred and trusted technology for electronically signing documents. Standards-Based
Signatures uses digital signature technology.What is eIDAS?On July 1, 2016 the enforcement of
EU Regulation No 910/2014 known as eIDAS (Electronic Identification and Trust Services) went
into effect, offering new promise for companies looking to adopt e-Signatures, whether inside
national borders or across multiple EU Member States. The new eIDAS regulation has clarified
three things:
That standard electronic signatures cannot be denied admissibility in court, subject to proofThe
minimum requirements for an eSignature to be an Advanced or Qualified eSignatureThat a QES
signature is equivalent to a handwritten signature and a QES signature from one member state
must be recognized across all EU member states.
The new eIDAS regulation has legally validated electronic signatures for most business use
cases, including in the most regulated industries of financial services, insurance, healthcare and

life sciences. It also mandates adoption by all 28 EU member states. This means that
companies will have an easier time than ever electronically transacting across EU borders with
their customers and partners. Docusign has been preparing to help our multinational and
European customers go digital under eIDAS for the last 3 years. [Key Resource: “eIDAS
Technical paper”]
What are the 3 levels of signatures defined by eIDAS?
The new eIDAS regulation divides electronic signatures into three types:
Different types of transactions require different types of signatures, as determined by each EU
member state’s national law. The eIDAS Regulation does not dictate when a signature is
actually needed for a transaction or what type of signature is necessary. This means that each
EU member state must specify in its laws when a particular transaction (i) cannot be signed
electronically or (ii) needs a higher form of electronic signature such as an advanced or qualified
electronic signature.For example, a temporary worker agreement requires a Qualified Electronic
Signature in Germany, whereas a Standard Electronic Signature suffices for a lunch catering
invoice.

A Qualified eSignature is required by law for certain use cases and is especially common in
Germany and Italy and for some use cases in France. Qualified eSignature carries with it the
highest levels of evidentiary support, but also significantly higher cost. Signers are required to
undertake face-to-face ID proofing before being issued a Qualified digital certificate, and the
time and cost can be prohibitive.

An Advanced eSignature is rarely required by law (although we have seen some exceptions in
Scotland and Hungary), but is often requested by regulated companies’ internal compliance
teams to manage company risk. An Advanced eSignature also needs a “chain of trust” (identity
proofing), which can be as simple as CRM information for B2B transactions, HR hiring process
for B2E transactions or individual ID proofing as part of a pre-established process for B2C
transactions. Unlike Qualified eSignatures, ID proofing can be done remotely and does not have
to be face-to-face.

Standard eSignature requires no ID proofing and is legal for most use cases, unless a different
signature type (including handwritten) is required by law. Both our Docusign Signature solution
and Express Signature solution are Standard eSignatures. Standard eSignatures have the
lowest cost, however, regulated companies may prefer a higher level of signature due to their
risk tolerance. It may also not always practical if a formal notarization or government registry is
required. Nevertheless, Standard eSignature is often the go-to-solution for nonregulated
industries in the EU because of the lack of signer friction involved.

Docusign offers 3 Cloud based EU Standards-Based Signatures

Express Signature

EU Advanced Signature

EU Qualified Signature

What is a TSP?TSP stands for "Trust Service Provider". As per eIDAS, a TSP is a provider who
delivers a “trust service” - in the case of our SBS offering, a digital signature associated with the
issuance of a digital certificate. In the context of our SBS suite there are two flavors of TSPs:
Docusign France, or a third party that is integrated through our TSP API in our signing
experience, in order to enable a signer to perform a digital signature with a specific credential.
What is the difference between Docusign as a TSP or a partner TSP?Docusign acts as a TSP
for Express and EU Advanced. However, some customers find limitations with these offerings:

Are operating in a geo/industry with unique preferences for a specific 3rd party TSP

Some customers object to being responsible for ID Proofing their signers (i.e., as a delegated
RA). Many TSPs offer ID Proofing services that remove the ID Proofing burden from the
customer.

As of the publish date of this document, Docusign does not yet offer our own QES solution.
Customers that require QES must purchase through a TSP Partner.

Why are we launching Docusign Standards-Based Signatures now?Ahead of eIDAS regulation
coming into force across the EU on July 1, 2016, Docusign is launching Standards-Based
Signatures. Prior to eIDAS, companies had to comply with the unique e-signature laws and
regulatory standards of each country, thereby limiting e-signature adoption and cross-border
digital transactions. eIDAS creates a common set of legal and technical standards for
e-signatures across the EU and paves the way for a single market for e-signature. What
problem does Docusign Standards-Based Signatures solve?Today, EU & global customers’
digital adoption is delayed because no e-signature solution currently offers robust, end-to-end
workflows and compliance with regional EU e-signature standards. With Docusign
Standards-Based Signatures, EU and global customers can automate agreements while
complying with regional EU e-signature standards. Customers can choose from
DocuSign-issued digital certificates or 3rd party-issued certificates from a Trust Service Provider
(“TSP”) they already use. When will Docusign Standards-Based Signatures be generally
available?Docusign Standards-Based Signatures will have a phased launch plan beginning in
June 2016 and extending into late 2016. Express Signature will be generally available in Q2, EU
Advanced Signature will be generally available in Q3, and EU Qualified Signature will be
generally available in Q4. Dates are subject to change. Does Docusign Standards-Based
Signatures work with the Classic Docusign Experience? No. To use Docusign Standards-Based
Signatures, users must be on the New Docusign Experience.
How does the solution work?Regardless of which Trust Service Provider is providing the
signature, the following process applies:

Step 1: Sending

The sender prepares the document to be signed. The only difference is that sender has to
specify the type of signature for the signer (click on More and select DS EU Advanced for
example) and to select how signer’s authentication will be done (either use access code or OTP
to be sent via SMS).

Step 2: Signing

The signer will receive a traditional Docusign notification email and follow the link to the
traditional Docusign signing experience. When signer has completed the doc through the New
Signing Experience and clicks on Continue (instead of Finish), the signer will continue with a
new modal prepared by the TSP to be able to perform the AES/QES signature. Signer
authentication will be done when that modal is shown to the signer. A digital certificate will be
used to perform the electronic signature to be embedded in the document.

The TSP is in charge of the authentication of the signer and the signature of the document.

Depending on the use cases, the TSP can be internal (Docusign France) or external (IDnow in
Germany, itAgile in Italy...).
What is the difference between CAdES and PAdES?The European Telecommunications
Standards Institute (ETSI) standard for PDF Advanced Electronic Signatures (PAdES) is a
complementary standard to the CMS Advanced Electronic Signature (CAdES) but specific to the
PDF format. Review the PAdES Standards (eIDAS) documentation on the ETSI website for
details. Visit the EU standards and specifications page to review other standards.
What does SBS work with? What doesn’t it work with?SBS is not compatible with the following
features:
NotaryLegacy digital signaturesMarkupOffline signingAllowing concatenation of signer
attachments
We do not let an account be provisioned with SBS if these features are enabled.The following
features work slightly differently with SBS:

Feature

Behavior without SBS

Behavior with SBS

Why?

Advanced Correct

Users can freely add/ remove recipients in work-flow without routing order being reset.

When new non-signature tab added, reset the flow back up to the first signature and remove
signatures. Warn the user that routing will restart.

SBS does not allow adding or removing of form fields after a digital signature has already been
applied to a PDF.

Free-form signing

All tags are allowed on free-form even after someone has signed.

Only allow Sig / Initials on free-form once someone has signed

If another signer has already signed the document, adding tabs other than signature tabs would
break the existing digital signatures on the document.

Downloading combined envelopes

Combined PDF is not digitally signed.

Combined PDF is not digitally signed.

Concatenating digitally signed PDFs breaks the digital signatures on the PDFs

Authoritative Copy

Downloading a copy of the document burns in a "COPY VIEW" watermark.

“COPY VIEW” is added as a PDF annotation (to indicate that the document being downloaded
is not the authoritative copy)

Burning the watermark into the PDF would break the digital signatures on the document.

Burning the watermark into the PDF would break the digital signatures on the document.

Wet-signing

Signers can print and sign the document manually at any time (with a physical pen).Then they
can scan and upload the document back into Docusign and keep business digital.

Wet signed documents are added as new documents to envelopes

This results in the uploaded or faxed, physically signed document being added as a new
document to the envelope. This new document gets only platform seal.

Attachment by Fax

Users can send attachments by fax

This option is disabled

The user is not considered to have signed the document until the attachment fax is received.
However, other signers can complete and sign the document while the fax is pending, meaning
the version of the document that the user ends up signing could be different than the version
that the user actually saw when they decided to sign it.

Tag value visibility

When using this feature, some data within tags may not be visible to any other signer or the
sender.

SBS will populate the tags if the "burn secure fields to initial PDF" on send.

Issue: There is an account setting to burn initial secure field values to the PDF. This allows
initial values set by a sender to be viewable by all recipients on an envelope (assuming they
have access to the document via doc visibility). If the tags aren't shared, and we aren't burning
values into the PDF, these values may not be visible during signing.
Change Signature while SigningRecipient can click on their adopted signature during the
Signing Ceremony and click Change to readopt the signature. The option for Change is
removed.The option for Change was removed from the menu due to an incompatibility with
SBS.Background and additional information can be found on this JIRA .Docusign for
SalesforceN/AThe options to select a digital signature type, or IDV, are not exposed in the UI. A
template creator would need to edit the template in the Web app to apply those settings. The
sender can also manually apply those settings at the time of sending via the embedded tagger
(field placement) page using the Actions menu -> “Edit Recipients” option to expose those
settings and apply what they need. Docusign Gen for SalesforceN/A If a Gen template is linked
with an EfS/DfS (Docusign for Salesforce) template, then SBS would be applied to the linked
EfS template. API sendingN/ASBS is fully compatible with API sending.
Where can I learn more about Docusign Standards-Based Signatures?If you have any
questions along the way, please see Demystifying the distinction between electronic and digital
signatures_EU Fit. Please check the “Docusign Standards-Based Signatures” Chatter group to
join in on all of the conversations around product announcements, questions, and upcoming
educational webinars.

