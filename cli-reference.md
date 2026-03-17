# Axigen CLI Reference (v10.6.30)


## Initial Context (Root)




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `LIST Domains [wildcard (ex: domain*)]` — lists the active domains of this server

- `LIST AllDomains [wildcard (ex: domain*)]` — lists all the domains (active and inactive) of this server

- `LIST domainActivationRequests` — lists the requests made for domain registration

- `CLEAR domainActivationRequests` — clear the list of requests not pending

- `SAVE CONFIG [<path>]` — saves the server's running configuration (a suffix will be added)

- `SAVE supportInfo [<path>]` — saves runtime information; default path is <workingDir>/supportInfo.zip

- `CONFIG SERVER` — enters the Server context

- `SET admin-password <password>` — sets the admin password (max. 32 chars) (OBSOLETE - kept for backward compatibility)

- `CHANGE password oldPassword <pass> newPassword <pass>` — changes your password (max. 32 chars)

- `LIST SecurityMethods` — list own security methods

- `REVOKE securityMethod <methodId>` — revokes the given security method

- `REVOKE all securityMethods` — revokes all security methods

- `SHOW twoFactorConfigured` — show own TwoFactor configuration status

- `SET twoFactorConfigured <yes|no>` — set own TwoFactor configuration status

- `SHOW onboardingComplete` — shows the value of the onboarding complete flag

- `SET onboardingComplete <yes|no>` — sets the onboarding complete flag

- `ENTER QUEUE` — enters the Queue context

- `ENTER AACL` — enters the Administrative ACL context

- `ENTER TRACER` — enters the Webdav tracer context

- `ENTER JSONQUERY` — enters the Json Query context

- `CREATE Domain name <name> domainLocation <path> wmFilterTemplatePath <sieve file path> postmasterPassword <pass>` — creates a domain

- `CREATE Subdomain prefix <name> parentDomain <name> postmasterPassword <pass>` — creates a subdomain

- `ENABLE Domain domainLocation <path>` — activates a domain to the server using the location parameter

- `ENABLE Domain name <name>` — activates a domain to the server using the name parameter

- `DISABLE Domain [name] <name>` — deactivates a domain from the server

- `EDIT Domain domainLocation <path>` — edits a domain from the server using the location parameter

- `EDIT Domain wmFilterTemplatePath <sieve file path>` — edits a domain from the server using the wmfilter template sieve file

- `EDIT Domain name <name>` — edits a domain from the server using the name parameter

- `DELETE Domain domainLocation <path> [dontKeepCopy]` — deletes a domain from the server using the location parameter

- `DELETE Domain name <name> [dontKeepCopy]` — deletes a domain from the server using the name parameter

- `UPDATE Domain [name] <domainName>` — updates a domain from the server

- `SHOW Domain [name] <domainName> [ATTR <param>]` — shows the given domain

- `RESTORE Domain name <domainName>` — restores a domain

- `SEARCH Object <objectNameOrId>[+<folderNameOrId>][@<domainName>] | +<folderNameOrId>[@<domainName>] | @<domainName>` — search for an object by name or id, displaying identity information in case it is found; ids must always be specified in hexa with '0x' prefix

- `LOOKUP Index Object <accountName>[+<folderName>]@<domainName>` — get the index files for an object

- `LOOKUP Index File <path>` — get the objects for an index file

- `LIST premiumAccounts [domain <name>] [wildcard (ex: account*)]` — lists the premium accounts (all or per domain)

- `SET premiumAccountAddons name <name> addons (list of addons)` — sets the addons for a premium account Possible addons: outlook|activesync|sharing|personalorganizer|ia

- `LIST premiumFolderRcpts [domain <name>] [wildcard (ex: account*)]` — lists the "premium" folder recipients (all or per domain)

- `SET premiumFolderRcptsAddons name <name> addons (list of addons)` — sets the addons for a "premium" folder recipient Possible addons: ia

- `SHOW LicenseInfo` — shows license information

- `SHOW PremiumAddonsStatistics` — shows the usage statistics for premium addons

- `SHOW AccountingStatistics [since <date>][until <date>]` — shows accounting statistics for the last month or a specified period

- `SHOW MigrationStatus` — shows migration status

- `PURGE public|account folders <folderName> [, <folderName>]* [<purgeCondition>]` — purge mails from specified folders of all users from all enabled domains

- `SET multilineEOF <string>` — set the EOF sequence for multi-line upload commands, defaults to .

- `ENABLE ExecutionTrace` — enable tracing of commands execution

- `DISABLE ExecutionTrace` — disable tracing of commands execution

- `EXPORT DOMAINDB <domainname>` — export domain dapi info to a database



## AACL




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — switches back to the previous context

- `DONE ` — switches back to the previous context

- `LIST resources` — lists all availablee resources

- `LIST admin-groups` — lists all available admin groups

- `LIST admin-users` — lists all available admin users

- `LIST server-principals` — lists all available server principals

- `LIST domain-principals [domain] <name>` — lists all available domain principals (per specific domain)

- `PURGE resources` — purge all resources

- `ADD admin-group [name] <name>` — adds a new admin group

- `UPDATE admin-group [name] <name>` — updates an admin group

- `REMOVE admin-group [name] <name> [forced]` — removes an admin group

- `SHOW admin-group [name] <name>` — shows admin group

- `ADD admin-user [name] <name> password <password>` — add a new admin user

- `UPDATE admin-user [name] <name>` — update an admin user

- `REMOVE admin-user [name] <name>` — remove an admin user

- `SHOW admin-user [name] <name>` — show admin user



## JSONQUERY




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `QUERY /domains` — retrieve domain metric info as json



## QUEUE




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — switches back to the previous context

- `FORCE QUEUE` — tries to force all mails in queue to be processed/sent

- `LIST ` — lists all queue entries

- `LIST ID <id>` — lists detailed information about a queue entry based on id

- `LIST FILTER <filters>` — lists the result of the filters applied on queue entries where <filters> can be a subset separated by spaces of the following: - $

- `RETRY <mailid>|lastFilter` — reschedules the mail with id <mailid>, or the mails matching the last "list filter" command

- `NDR <mailid>|lastFilter` — send ndr for the mail with id <mailid>, or the mails matching the last "list filter" command

- `DELETE <mailid>|lastFilter` — delete the mail with id <mailid>, or the mails matching the last "list filter" command

- `ENTER QUARANTINE` — enters the quarantine context

- `ENABLE PROCESSING DEBUG` — Start debugging mode for processing module

- `DISABLE PROCESSING DEBUG` — Stop debugging mode for processing module

- `CONTINUE PROCESSING DEBUG` — Perform another processing step



## QUEUE/QUARANTINE




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — switches back to the previous context

- `LIST ` — lists all queue entries

- `LIST ID <id>` — lists detailed information about a queue entry based on id

- `LIST FILTER <filters>` — lists the result of the filters applied on queue entries where <filters> can be a subset separated by spaces of the following: - $

- `DELIVER <mailid>|lastFilter` — delivers the mail with id <mailid>, or the mails matching the last "list filter" command

- `DELETE <mailid>|lastFilter` — delete the mail with id <mailid>, or the mails matching the last "list filter" command



## SERVER




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SAVE Config [<path>]` — saves the server's running configuration (a suffix will be added)

- `SHOW Config` — shows the entire server's running configuration

- `SHOW StorageInformation [details]` — shows storage files information (with details per file if option present)

- `SHOW StorageStatistics [details|summary][average][raw][mboxDetails][mboxReset]` — shows total or average storage statistics (with details per file if option present)

- `SHOW DisposableMetadataInformation` — shows information about the size occupied by obsolete disposable meta-data in the storage

- `SHOW BrandingElement <faviconPhoto|faviconNPhoto|ajaxPublicPhoto|ajaxPrivatePhoto|standardPublicPhoto|standardPrivatePhoto|mobilePublicPhoto|mobilePrivatePhoto|*>` — shows the binary value of a branding element (base64 encoded)

- `SET [primaryDomain <name>]` — sets the server's primary domain

- `SET [caBundlePath <file>]` — sets file for root Certificate Authority bundle

- `SET [sslRandomFile <file>]` — sets file for entropy data used when generating random

- `SET [enableIOSynchronization <yes|no>]` — enables/disables the I/O synchronization for file storages

- `SET [defaultTimezone <timezone>]` — sets the default timezone

- `SET [defaultLanguage <lang>]` — sets the default language

- `SET [autodetectLanguage <yes|no>]` — Enable/Disable language autodetection

- `SET [allowedLanguages "<lang>[ <lang>]*"]` — sets the list of allowed languages; empty list means allow all

- `SET [serverName <name>]` — sets the server name

- `SET [pushNotificationGeneratorPath <path>]` — sets the path to be used by the push notification generator to dump json files

- `SET [maxIndexingThreads <no.>]` — sets the maximum number of threads for the search indexing service

- `SET [sendStatisticsEmail <yes|no>]` — Enable/Disable sending of monthly statistics email to axigen headquarters

- `SET [postmasterStatisticsEmailAddress <email>]` — Sent email address where a copy of monthly statistics email will be sent

- `SET [enableStorageStatistics <yes|no>]` — Enable/Disable storage statistics for newly registered storage units

- `SET [brandingName <name>]` — sets the server branding name

- `SET [enableTnefCommand <yes|no>]` — Enable/Disable tnef

- `SET [allowAliasLogins <yes|no>]` — Allow/Prevent logins using alias account or domain names

- `SET [pop3ExclusiveLock <yes|no>]` — Prevent/Allow multiple POP3 clients from accessing the same maildrop

- `SET [enableSRS <yes|no>]` — enables/disables sender rewriting scheme

- `SET [srsSecretKey <key>]` — sets the sender rewriting scheme secret key

- `SET [searchIndexOptimizeThreshold <count>]` — sets number of fts updates which triggers a search index optimization

- `SET [searchIndexVacuumAbsoluteThreshold <count>]` — sets number of freelist pages which triggers a search index vacuum

- `SET [searchIndexVacuumRelativeThreshold <precent>]` — sets percent of freelist pages which triggers a search index vacuum

- `SET [searchIndexTokenizer <defaut|mecab>]` — sets the tokenizer used by search indexes

- `SET [enableConversationIndexDefault <yes|no>]` — sets the default value for the conversation index for new domains

- `SET [indexAutoRescheduleTimeout <never | apocalypse | <delay in seconds>>]` — sets value used by mailsearch/sort/conv index jobs for automatic rescheduling after execution. Explicit values can be between 1 and 2147483647

- `SET [serverSecretKey <key>]` — configure server secret key (min. 32 chars)

- `SET [emailSampleCollection ([antiSpamFalseNegative] [antiSpamFalsePositive]) | all]` — sets list of triggers for collecting email samples. Option 'all' turn on everything

- `SET [emailSampleCollectionPath <path>]` — sets the path on disk where to collect the email samples

- `SET [emailSampleRetentionPeriod <days>]` — sets the retention period for collected samples

- `SET [templatesPath <path>]` — sets the path to the template files

- `ESET BrandingElement <faviconPhoto|faviconNPhoto|ajaxPublicPhoto|ajaxPrivatePhoto|standardPublicPhoto|standardPrivatePhoto|mobilePublicPhoto|mobilePrivatePhoto|webadminFaviconPhoto|webadminPublicPhoto|webadminPrivatePhoto|*>` — sets the server binary value of a branding element (the value must be base64 encoded)

- `RESET ` — resets the service to the currently active configuration

- `CONFIG LOG` — enters the Log context

- `CONFIG CLI` — enters the CLI context

- `CONFIG RPOP` — enters the RPOP context

- `CONFIG SMTP-INCOMING` — enters the SMTP-Incoming context

- `CONFIG SMTP-OUTGOING` — enters the SMTP-Outgoing context

- `CONFIG PROCESSING` — enters the Processing context

- `CONFIG POP3` — enters the POP3 context

- `CONFIG IMAP` — enters the IMAP context

- `CONFIG WEBMAIL` — enters the Webmail context

- `CONFIG WEBADMIN` — enters the Webadmin context

- `CONFIG FTP-BACKUP` — enters the FTP-Backup context

- `CONFIG DNR` — enters the DNR context

- `CONFIG REPORT` — enters the Report context

- `CONFIG POP3-Proxy` — enters the POP3 Proxy context

- `CONFIG IMAP-Proxy` — enters the IMAP Proxy context

- `CONFIG WEBMAIL-Proxy` — enters the Webmail Proxy context

- `CONFIG USERDB` — enters the User Database context

- `CONFIG PERMISSIONS` — enters the Permissions context

- `CONFIG FILTERS` — enters the Filters context

- `CONFIG MOBILITY` — enters the Mobility context

- `CONFIG CLUSTER` — enters the Cluster configuration context

- `CONFIG InitialAccountSettings` — enters the initial account settings context

- `CONFIG AUTODISCOVERY` — enters the Autodiscovery configuration context

- `CONFIG CERTS` — enters the Certificates configuration context

- `CONFIG CALLOG` — enters the Calendar Log configuration context

- `CONFIG SECURITY` — enters the Security configuration context

- `CONFIG JOBLOG` — enters the JobLog configuration context

- `CONFIG MAILBOXAPI` — enters the Mailbox API configuration context

- `CONFIG SRVLOG` — enters the Server Log configuration context

- `LIST Storages [matchingURI <pattern>]` — list all or some storage units registered to AXIGEN; an optional pattern used for filtering based on storage URI can be provided

- `LIST activeStorageTransactions [matchingURI <pattern>] [details]` — list active transactions on all or some storage units registered to AXIGEN; an optional pattern used for filtering based on storage URI can be provided; without 'details' argument only the total active transactions list is reported

- `READLOCK Storages [matchingURI <pattern>]` — acquire read lock on all or some storage units registered to AXIGEN; an optional pattern used for filtering based on storage URI can be provided

- `READUNLOCK Storages [matchingURI <pattern>]` — release read lock on all or some storage units registered to AXIGEN; an optional pattern used for filtering based on storage URI can be provided

- `COMPACT ServerStorage [forced]` — compact server storage container files; if 'forced' option is used, the container files will be compacted even if they do not report too much free space available

- `COMPACT attach | peek [timeout]` — permanently or temporarily attach to another CLI session where compact is running for the server storage

- `COMPACT abort` — abort a running compact job for the server storage started from another CLI session

- `LIST Usermaps` — shows the list of usermaps

- `ADD Usermap [name] <name>` — adds an usermap to the service

- `UPDATE Usermap [name] <name>` — updates an usermap from the service

- `REMOVE Usermap [name] <name>` — removes an usermap from the service

- `SHOW Usermap [name] <name> [ATTR <param>]` — shows the given usermap

- `UPDATE SmtpFilters [<path>]` — update smtp filters file with the contents of the file specified by path or sent directly via CLI connection

- `SHOW SmtpFilters [<path>]` — download smtp filters file to the file specified by path or directly via CLI connection

- `ENABLE [detailed] [mbox] StorageStatistics` — enables I/O statistics for all storages

- `DISABLE StorageStatistics` — disable I/O statistics for all storages

- `ADD smsConnector [name] <name>` — add a new SMS connector

- `LIST smsConnectors` — list all SMS connectors

- `UPDATE smsConnector [name] <name>` — updates an SMS connector

- `SHOW smsConnector [name] <name> [[ATTR] <param>]` — shows the given SMS connector

- `REMOVE smsConnector [name] <name>` — removes the named connector



## SERVER/AUTODISCOVERY




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET enableIMAPAutodiscovery <yes|no>` — enables/disables IMAP Autodiscovery

- `SET enablePOP3Autodiscovery <yes|no>` — enables/disables POP3 Autodiscovery

- `SET enableSMTPAutodiscovery <yes|no>` — enables/disables SMTP Autodiscovery

- `SET enableWebdavAutodiscovery <yes|no>` — enables/disables WEBDAV Autodiscovery

- `CONFIG defaultUrls` — enters the autodiscoveryDefaultUrls context

- `SHOW defaultUrls` — shows default autodiscovery URLs



## SERVER/AUTODISCOVERY/defaultUrls




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET httpAutodiscoveryUrl <url>` — set the http autodiscovery url

- `SET imapAutodiscoveryUrl <url>` — set the imap autodiscovery url

- `SET pop3AutodiscoveryUrl <url>` — set the pop3 autodiscovery url

- `SET smtpAutodiscoveryUrl <url>` — set the smtp autodiscovery url

- `SET webdavAutodiscoveryUrl <url>` — set the webdav autodiscovery url



## SERVER/CALLOG




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SAVE Config` — saves the server's running configuration

- `SET [logLevel <level>]` — sets the service's logging level

- `SET [logType <type>]` — sets the service's logging type

- `SET [logHost <host>]` — sets the service's remote logging host

- `RESET ` — resets the service to the currently active configuration



## SERVER/CERTS




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `GENERATE letsencrypt hostname <hostname> terms accept|yes [contact <email>]` — Obtain DV certificate for a hostname from LetsEncrypt servers; using this command requires agreement to the LetsEncrypt terms of service

- `REVOKE letsencrypt hostname <hostname>` — Revoke DV certificate for a hostname from LetsEncrypt servers



## SERVER/CLI




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SAVE Config` — saves the server's running configuration

- `LIST Listeners` — lists available listeners

- `START Service` — starts the cli service

- `STOP Service` — stops the cli service

- `SET [maxErrors <maxErrors>]` — sets max no. of wrong commands

- `SET [maxAuthErrors <maxErrors>]` — sets max no. of failed authentications

- `SET [maxAuthCommands <maxCmds>]` — sets max no. of commands that can be issued before authentication

- `SET [maxConnThreads <maxThreads>]` — sets max no. of threads handling the conn.

- `SET [minConnThreads <minThreads>]` — sets min no. of threads handling the conn.

- `SET [logLevel <level>]` — sets the service's logging level

- `SET [logType <type>` — 



## SERVER/CLUSTER




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SHOW STATUS` — Show cluster database statistics

- `SHOW configSynchronizer <configSynchronizerName>` — Display current status of a synchronization job

- `SET runMode <standAlone|frontEnd|backEnd>` — set current machine running mode in cluster

- `SET clusterKey <string>` — Set the key used to identify machines belonging to the same cluster

- `LIST clusterAddresses` — List addresses of machines in cluster

- `LIST userMap cache` — List entries in user map cache

- `LIST hostDefinition cache` — List entries in host definition cache

- `LIST configSynchronizers` — List registered cluster configuration synchronizing jobs

- `ADD clusterAddress <address>` — Add a machine to cluster

- `REMOVE clusterAddress <address>` — Remove a machine from cluster

- `UPDATE userMap cache [userAddres [userAddress...]]` — Update entries in user map cache

- `UPDATE hostDefinition cache [hostAddress [hostAddress...]]` — Update entries in host definition cache

- `UPDATE config <configSynchronizerName>` — Push local configuration to all cluster nodes

- `JOIN <clusterKey> runMode <frontEnd|backEnd> [via <hostAddress>] [as <selfHostAddress>] [waitSync]` — Join or create a cluster



## SERVER/DNR




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SAVE Config` — saves the server's running configuration

- `LIST Nameservers` — lists the nameservers

- `EMPTYCACHE ` — empties the cache

- `QUERY A <domain.name>` — queries A entries for the provided domain using the DNR service

- `QUERY MX <domain.name>` — queries MX entries for the provided domain using the DNR service

- `QUERY NS <domain.name>` — queries NS entries for the provided domain using the DNR service

- `QUERY TXT <domain.name>` — queries TXT entries for the provided domain using the DNR service

- `QUERY PTR <ip.address>` — queries PTR entries for the provided ip address using the DNR service

- `QUERY AAAA <domain.name>` — queries AAAA entries for the provided domain using the DNR service

- `SET [timeout <timeout>]` — sets the timeout

- `SET [retries <retries>]` — sets the number of retries

- `SET [cacheSize <cacheSize>]` — sets the cache size

- `SET [logLevel <level>]` — sets the service's logging level

- `SET [logType <type>]` — sets the service's logging type

- `SET [logHost <host>]` — sets the service's remote logging host

- `RESET ` — resets the service to the currently active configuration

- `ADD Nameserver [priority] <priority>` — adds a nameserver to the service

- `UPDATE Nameserver [priority] <priority>` — updates a nameserver from the service

- `REMOVE Nameserver [priority] <priority>` — removes a nameserver from the service

- `SHOW Nameserver [priority] <priority> [ATTR <param>]` — shows the given nameserver

- `REMOVE All` — removes all nameservers from the service



## SERVER/FILTERS




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `LIST ScriptFilters` — lists the script filters defined

- `LIST SocketFilters` — lists the socket filters defined

- `LIST IntegratedFilters` — lists the integrated filters defined

- `LIST ActiveFilters` — lists the active filters

- `LIST Filters` — lists all four categories of filters

- `SET [logLevel <level>]` — sets the service's logging level

- `SET [logType <type>]` — sets the service's logging type

- `SET [logHost <host>]` — sets the service's remote logging host

- `ADD ScriptFilter [name] <name> file <file>` — adds a script filter

- `UPDATE ScriptFilter [name] <name>` — updates a script filter

- `REMOVE ScriptFilter [name] <name>` — removes a script filter from the list

- `SHOW ScriptFilter [name] <name> [ATTR <param>]` — shows the given script filter

- `ADD SocketFilter [name] <name> address <addr> protocolFile <file>` — adds a socket filter

- `UPDATE SocketFilter [name] <name>` — updates a socket filter

- `REMOVE SocketFilter [name] <name>` — removes a socket filter from the list

- `SHOW SocketFilter [name] <name> [ATTR <param>]` — shows the given socket filter

- `ADD IntegratedFilter [name] <name> type <type> command <command>` — adds a integrated filter

- `UPDATE IntegratedFilter [name] <name>` — updates a integrated filter

- `REMOVE IntegratedFilter [name] <name>` — removes a integrated filter from the list

- `SHOW IntegratedFilter [name] <name> [ATTR <param>]` — shows the given integrated filter

- `ADD ActiveFilter [priority] <no.> filterName <name> filterType <type>` — adds an active filter to the active filter list

- `UPDATE ActiveFilter [priority] <no.>` — updates a filter

- `REMOVE ActiveFilter [priority] <no.>` — removes a filter from the active filter list

- `SHOW ActiveFilter [priority] <no.> [ATTR <param>]` — shows the given filter

- `LIST Whitelist` — list address patterns from Whitelist (available only for the accounts context)

- `ADD Whitelist <address_pattern>` — add an address pattern to Whitelist (available only for the accounts context)

- `REMOVE Whitelist <address_pattern>` — remove an address pattern from Whitelist (available only for the accounts context)

- `RESET Whitelist` — remove all address patterns from Whitelist (available only for the accounts context)

- `LIST Blacklist` — list address patterns from Blacklist (available only for the accounts context)

- `ADD Blacklist <address_pattern>` — add an address pattern to Blacklist (available only for the accounts context)

- `REMOVE Blacklist <address_pattern>` — remove an address pattern from Blacklist (available only for the accounts context)

- `RESET Blacklist` — remove all address patterns from Blacklist (available only for the accounts context)



## SERVER/FILTERS/ActiveFilter




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [priority <priority>]` — sets the priority of the filter - only usable in an UPDATE operation

- `SET [filterName <name>]` — sets the name of the filter as defined in the socket/script object sets

- `SET [filterType <type>]` — sets type of the filter (to which object set belongs)

- `SET [applyOn (local relay localOnCluster relayFromCluster)]` — Specifies where this filter is activated (local, relay delivery or both)



## SERVER/FTP-BACKUP




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SAVE Config` — saves the server's running configuration

- `LIST Listeners` — lists available listeners

- `START Service` — starts the ftp backup service

- `STOP Service` — stops the ftp backup service

- `SET [maxErrors <maxErrors>]` — sets max no. of wrong commands

- `SET [maxAuthErrors <maxErrors>]` — sets max no. of failed authentications

- `SET [maxConnThreads <maxThreads>]` — sets max no. of threads handling the conn.

- `SET [minConnThreads <minThreads>]` — sets min no. of threads handling the conn.

- `SET [logLevel <level>]` — sets the service's logging level

- `SET [logType <type>]` — sets the service's logging type

- `SET [logHost <host>]` — sets the service's remote logging host

- `SET [messagesTarEnabled <yes|no>]` — enables/disables tar archive on messages

- `SET [nameEncoding <utf7|utf8>]` — sets name encoding for path names

- `CONFIG AccessControl` — enters the AccessControl context

- `RESET ` — resets the service to the currently active configuration

- `ADD Listener [address] <address>` — adds a listener to the service

- `UPDATE Listener [address] <address>` — updates a listener from the service

- `REMOVE Listener [address] <address>` — removes a listener from the service

- `SHOW Listener [address] <address> [ATTR <param>]` — shows the given listener

- `FILESYSTEM mount <mountPoint> [since <backupLabel>] [backup <backupLabel>] [noremoved] [domain <name>]` — 

- `FILESYSTEM mount <mountPoint> [since <backupLabel>] [backup <backupLabel>] [noremoved] domain <name> publicFolder [<folderPath>]` — 

- `FILESYSTEM mount <mountPoint> [since <backupLabel>] [backup <backupLabel>] [noremoved] domain <name> object <name> [folder <folderPath>]` — 

- `FILESYSTEM unmount <mountPoint>` — 

- `FILESYSTEM status [<mountPoint>]` — 

- `REMOVE BACKUP <backupLabel> [from domain <name>]` — 

- `LIST BACKUPS [from domain <name>]` — 

- `PURGE BACKUPS [from domain <name>]` — 



## SERVER/FTP-BACKUP/AccessControl




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `LIST AllowRules` — lists the allow rules for this listener

- `LIST DenyRules` — lists the deny rules for this listener

- `SET [maxConnections <maxConn>]` — sets max number of connections

- `SET [timeInterval <interval>]` — sets the time interval

- `SET [maxIntervalConnections <interval>]` — sets max connections in time interval

- `SET [peerMaxConnections <maxConn>]` — sets sets max connections no. from a single host

- `SET [peerTimeInterval <interval>]` — sets the time interval - single host

- `SET [peerMaxIntervalConnections <interval>]` — sets max connections in time interval - single host

- `ADD DenyRule [ipSet] <ipRange> [enable <yes|no>] [priority <priority>]` — adds a deny rule to the listener

- `UPDATE DenyRule [ipSet] <ipRange> [enable <yes|no>] [priority <priority>]` — updates a deny rule from the listener

- `REMOVE DenyRule [ipSet] <ipRange>` — removes a deny rule from the listener

- `SHOW DenyRule [ipSet] <ipRange>` — shows the given rule

- `ADD AllowRule [ipSet] <ipRange>` — adds an allow rule to the listener

- `UPDATE AllowRule [ipSet] <ipRange>` — updates an allow rule from the listener

- `REMOVE AllowRule [ipSet] <ipRange>` — removes an allow rule from the listener

- `SHOW AllowRule [ipSet] <ipRange>` — shows the given rule



## SERVER/IMAP




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SAVE Config` — saves the server's running configuration

- `LIST Listeners` — lists available listeners

- `START Service` — starts the imap service

- `STOP Service` — stops the imap service

- `SET [maxErrors <maxErrors>]` — sets max no. of wrong commands

- `SET [maxAuthErrors <maxErrors>]` — sets max no. of failed authentications

- `SET [maxConnThreads <maxThreads>]` — sets max no. of threads handling the conn.

- `SET [minConnThreads <minThreads>]` — sets min no. of threads handling the conn.

- `SET [logLevel <level>]` — sets the service's logging level

- `SET [logType <type>]` — sets the service's logging type

- `SET [logHost <host>]` — sets the service's remote logging host

- `SET [allowStartTLS <yes|no>]` — allow/not allow secure connections

- `SET [secureConnAuthTypes (types)]` — sets types of authentication on secure conn.

- `SET [plainConnAuthTypes (types)]` — sets types of authentication on plain conn.

- `SET [secureConnAllowLogin <yes|no>]` — allow/not allow plain text login on secure conn.

- `SET [plainConnAllowLogin <yes|no>]` — allow/not allow plain text login on plain conn.

- `SET [userdbConnectorType <type>]` — sets the type of the userdb connector

- `SET [userdbConnectorName <name>]` — sets the name of the userdb connector

- `SET [greetingsText <text>]` — sets the greeting text for this service

- `SET [imapIdEnabled <yes|no>]` — answer/do not answer to IMAP ID commands

- `SET [imapShowAllFolders <yes|no>]` — list shows all folders or just the mail ones

- `CONFIG AccessControl` — enters the AccessControl context

- `RESET ` — resets the service to the currently active configuration

- `ADD Listener [address] <address>` — adds a listener to the service

- `UPDATE Listener [address] <address>` — updates a listener from the service

- `REMOVE Listener [address] <address>` — removes a listener from the service

- `SHOW Listener [address] <address> [ATTR <param>]` — shows the given listener



## SERVER/IMAP-Proxy




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SAVE Config` — saves the server's running configuration

- `LIST Listeners` — lists available listeners

- `START Service` — starts the imap proxy service

- `STOP Service` — stops the imap proxy service

- `SET [maxErrors <maxErrors>]` — sets max no. of wrong commands

- `SET [maxAuthErrors <maxErrors>]` — sets max no. of failed authentications

- `SET [maxConnThreads <maxThreads>]` — sets max no. of threads handling the conn.

- `SET [minConnThreads <minThreads>]` — sets min no. of threads handling the conn.

- `SET [logLevel <level>]` — sets the service's logging level

- `SET [logType <type>]` — sets the service's logging type

- `SET [logHost <host>]` — sets the service's remote logging host

- `SET [allowStartTLS <yes|no>]` — allow/not allow secure connections

- `SET [userdbConnectorType <type>]` — sets the type of the userdb connector

- `SET [userdbConnectorName <name>]` — sets the name of the userdb connector

- `SET [authenticateOnProxy <yes|no>]` — specifies if user authentication should be done also on proxy

- `SET [greetingsText <text>]` — sets the greeting text for this service

- `SET [imapIdEnabled <yes|no>]` — answer/do not answer to IMAP ID comands

- `RESET ` — resets the service to the currently active configuration

- `CONFIG AccessControl` — enters the AccessControl data context

- `CONFIG connectionData` — enters the connection data context

- `CONFIG mappingData` — enters the mapping data context

- `ADD Listener [address] <address>` — adds a listener to the service

- `UPDATE Listener [address] <address>` — updates a listener from the service

- `REMOVE Listener [address] <address>` — removes a listener from the service

- `SHOW Listener [address] <address> [ATTR <param>]` — shows the given listener



## SERVER/IMAP-Proxy/AccessControl




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `LIST AllowRules` — lists the allow rules for this listener

- `LIST DenyRules` — lists the deny rules for this listener

- `SET [maxConnections <maxConn>]` — sets max number of connections

- `SET [timeInterval <interval>]` — sets the time interval

- `SET [maxIntervalConnections <interval>]` — sets max connections in time interval

- `SET [peerMaxConnections <maxConn>]` — sets sets max connections no. from a single host

- `SET [peerTimeInterval <interval>]` — sets the time interval - single host

- `SET [peerMaxIntervalConnections <interval>]` — sets max connections in time interval - single host

- `ADD DenyRule [ipSet] <ipRange> [enable <yes|no>] [priority <priority>]` — adds a deny rule to the listener

- `UPDATE DenyRule [ipSet] <ipRange> [enable <yes|no>] [priority <priority>]` — updates a deny rule from the listener

- `REMOVE DenyRule [ipSet] <ipRange>` — removes a deny rule from the listener

- `SHOW DenyRule [ipSet] <ipRange>` — shows the given rule

- `ADD AllowRule [ipSet] <ipRange>` — adds an allow rule to the listener

- `UPDATE AllowRule [ipSet] <ipRange>` — updates an allow rule from the listener

- `REMOVE AllowRule [ipSet] <ipRange>` — removes an allow rule from the listener

- `SHOW AllowRule [ipSet] <ipRange>` — shows the given rule



## SERVER/IMAP-Proxy/connectionData




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — switches back to the previous context (does not cancel changes)

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [rwTimeout <no.>]` — sets the timeout for the read/write operation

- `SET [maxConnections <no.>]` — sets the maximum number of simultaneous connections made to AXIGEN backservers

- `SET [sslEnable <yes|no>]` — specifies if the connection should be SSL

- `SET [localInterface <interface>]` — specifies the address of the interface used to make the connections



## SERVER/IMAP-Proxy/mappingData




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — switches back to the previous context (does not cancel changes)

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [userMap <map>]` — a userMap from the list defined on the server

- `SET [mappingHost <host>]` — sets the name or IP address of a default AXIGEN machine to be used if userMap is set to none

- `SET [mappingPort <port>]` — sets the port on which to connect to the default AXIGEN machine



## SERVER/IMAP/AccessControl




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `LIST AllowRules` — lists the allow rules for this listener

- `LIST DenyRules` — lists the deny rules for this listener

- `SET [maxConnections <maxConn>]` — sets max number of connections

- `SET [timeInterval <interval>]` — sets the time interval

- `SET [maxIntervalConnections <interval>]` — sets max connections in time interval

- `SET [peerMaxConnections <maxConn>]` — sets sets max connections no. from a single host

- `SET [peerTimeInterval <interval>]` — sets the time interval - single host

- `SET [peerMaxIntervalConnections <interval>]` — sets max connections in time interval - single host

- `ADD DenyRule [ipSet] <ipRange> [enable <yes|no>] [priority <priority>]` — adds a deny rule to the listener

- `UPDATE DenyRule [ipSet] <ipRange> [enable <yes|no>] [priority <priority>]` — updates a deny rule from the listener

- `REMOVE DenyRule [ipSet] <ipRange>` — removes a deny rule from the listener

- `SHOW DenyRule [ipSet] <ipRange>` — shows the given rule

- `ADD AllowRule [ipSet] <ipRange>` — adds an allow rule to the listener

- `UPDATE AllowRule [ipSet] <ipRange>` — updates an allow rule from the listener

- `REMOVE AllowRule [ipSet] <ipRange>` — removes an allow rule from the listener

- `SHOW AllowRule [ipSet] <ipRange>` — shows the given rule



## SERVER/IMAP/AccessControl/AllowRule




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [ipSet <ipSet>]` — sets the ipSet parameter - only usable in an UPDATE operation

- `SET [enable <yes|no>]` — enable/disable the rule

- `SET [priority <priority>]` — sets the rule's priority

- `SET [maxConnections <maxConn>]` — sets max number of connections

- `SET [timeInterval <interval>]` — sets the time interval

- `SET [maxIntervalConnections <interval>]` — sets max connections in time interval

- `SET [peerMaxConnections <maxConn>]` — sets sets max connections no. from a single host

- `SET [peerTimeInterval <interval>]` — sets the time interval - single host

- `SET [peerMaxIntervalConnections <interval>]` — sets max connections in time interval - single host



## SERVER/InitialAccountSettings




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [weekStartDay <sunday|monday|tuesday|wednesday|thursday|friday|saturday>]` — sets the week start day

- `SET [workingDays <(sunday monday tuesday wednesday thursday friday saturday)>]` — sets working days mask

- `SET [startWorkingTime  <hh:mm[:ss]>]` — sets daily start working time

- `SET [endWorkingTime <hh:mm[:ss]>]` — sets daily end working time

- `SET [dateFormat <new format>]` — sets format for displaying dates

- `SET [timeFormat <new format>]` — sets format for displaying times

- `SET [calendarType <gregorian|persian>]` — sets the calendar type

- `SET [autoAddRecipients <yes|no>]` — sets flag for automatically adding recipients from sent mails to the Collected Addresses folder



## SERVER/JOBLOG




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SAVE Config` — saves the server's running configuration

- `SET [logLevel <level>]` — sets the service's logging level

- `SET [logType <type>]` — sets the service's logging type

- `SET [logHost <host>]` — sets the service's remote logging host

- `RESET ` — resets the service to the currently active configuration



## SERVER/LOG




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SAVE Config` — saves the server's running configuration

- `LIST Listeners` — lists available listeners

- `LIST Rules` — lists rules

- `START Service` — starts the log service

- `STOP Service` — stops the log service

- `SET [enableSecurityLog <yes|no>]` — enable/disable the security log

- `SET [logLevel <level>]` — sets the service's logging level

- `SET [logType <type>]` — sets the service's logging type

- `SET [logHost <host>]` — sets the service's remote logging host

- `RESET ` — resets the service to the currently active configuration

- `ADD Listener [address] <address>` — adds a listener to the service

- `UPDATE Listener [address] <address>` — updates a listener from the service

- `REMOVE Listener [address] <address>` — removes a listener from the service

- `SHOW Listener [address] <address> [ATTR <param>]` — shows the given listener

- `ADD Rule [priority] <priority>` — adds a rule

- `UPDATE Rule [priority] <priority>` — updates a rule

- `REMOVE Rule [priority] <priority>` — removes a rule

- `SHOW Rule [priority] <priority> [ATTR <param>]` — shows the given rule



## SERVER/MAILBOXAPI




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SAVE Config` — saves the server's running configuration

- `SET [logLevel <level>]` — sets the service's logging level

- `SET [logType <type>]` — sets the service's logging type

- `SET [logHost <host>]` — sets the service's remote logging host

- `RESET ` — resets the service to the currently active configuration



## SERVER/MOBILITY




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [enableMobileWebmail <yes|no>]` — enables/disables mobile webmail

- `SET [enableActiveSync <yes|no>]` — enables/disables activeSync



## SERVER/PERMISSIONS




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — switches back to the previous context

- `DONE ` — switches back to the previous context

- `LIST Permissions` — lists all available permissions

- `GRANT permission (<permNames>) admin-user [name] <name>` — grants permissions to user

- `REVOKE permission (<permNames>) admin-user [name] <name>` — revokes permissions to user

- `DENY permission (<permNames>) admin-user [name] <name>` — denies permissions to user

- `GRANT permission (<permNames>) admin-group [name] <name>` — grants permissions to group

- `REVOKE permission (<permNames>) admin-group [name] <name>` — revokes permissions to group

- `DENY permission (<permNames>) admin-group [name] <name>` — denies permissions to group permissions:  - manageServerConfig manageServerFilters manageCluster manageProcessing manageLog manageDNR manageSMTPIn manageSMTPOut managePOP3 manageIMAP manageWebMail manageRPOP managePOP3Proxy manageIMAPProxy manageWebmailProxy manageCLI manageWebAdmin manageFTPBackup manageReporting accessDumpData manageAuthentication activateAnyDomain manageConfigOnAnyDomain manageFiltersOnAnyDomain backupAnyDomain restoreAnyDomain deactivateAnyDomain manageAdminLimitsOnAnyDomain manageServicesOnAnyDomain manageCatchAllOnAnyDomain manageGroupwareOnAnyDomain manageLdapSyncOnAnyDomain manageDomainAliasesOnAnyDomain manageDomainStorageOnAnyDomain manageAccountServicesOnAnyDomain manageAutomaticMigrationOnAnyDomain manageFoldersQuotasOnAnyDomain managePasswordPolicyOnAnyDomain manageWebmailLimitsOnAnyDomain manageFilteredEmailOnAnyDomain manageSendReceiveRestrictionsOnAnyDomain manageRPOPRestrictionsOnAnyDomain manageTemporaryAddressesOnAnyDomain manageAccountRecoveryOnAnyDomain managePersonalOrganizerOnAnyDomain manageSharingOnAnyDomain manageOutlookConnectorOnAnyDomain manageActiveSyncOnAnyDomain manageIAOnAnyDomain manageAccountsOnAnyDomain createAccountsOnAnyDomain removeAccountsOnAnyDomain manageAccountsNamingOnAnyDomain changeAccountsPasswordOnAnyDomain changeAccountsClassOnAnyDomain manageAccountsContactInformationOnAnyDomain manageAccountsWebmailOptionsOnAnyDomain manageGroupsOnAnyDomain createGroupsOnAnyDomain removeGroupsOnAnyDomain manageGroupsNamingOnAnyDomain manageGroupsMembersOnAnyDomain manageMaillistsOnAnyDomain createMailListsOnAnyDomain removeMailListsOnAnyDomain manageMailListsNamingOnAnyDomain changeMailListsPasswordOnAnyDomain manageMailListsMemberOnAnyDomain manageMailListsSubscriptionOnAnyDomain manageMailListsPostingOnAnyDomain manageMailListsMessageHeadersOnAnyDomain manageMailListsTemplatesOnAnyDomain manageMailListsWebmailOptionsOnAnyDomain manageMailListsServicesOnAnyDomain manageMailListsFoldersQuotasOnAnyDomain manageMailListsWebmailLimitsOnAnyDomain manageMailListsSendReceiveRestrictionsOnAnyDomain manageAccountClassesOnAnyDomain createAccountClassesOnAnyDomain removeAccountClassesOnAnyDomain renameAccountClassesOnAnyDomain manageFolderRecipientsOnAnyDomain managePublicFolderOnAnyDomain createPublicFolderOnAnyDomain removePublicFolderOnAnyDomain renamePublicFolderOnAnyDomain managePublicFoldersQuotasOnAnyDomain manageAdminACL



## SERVER/POP3




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SAVE Config` — saves the server's running configuration

- `LIST Listeners` — lists available listeners

- `START Service` — starts the pop3 service

- `STOP Service` — stops the pop3 service

- `SET [maxErrors <maxErrors>]` — sets max no. of wrong commands

- `SET [maxAuthErrors <maxErrors>]` — sets max no. of failed authentications

- `SET [maxConnThreads <maxThreads>]` — sets max no. of threads handling the conn.

- `SET [minConnThreads <minThreads>]` — sets min no. of threads handling the conn.

- `SET [logLevel <level>]` — sets the service's logging level

- `SET [logType <type>]` — sets the service's logging type

- `SET [logHost <host>]` — sets the service's remote logging host

- `SET [allowStartTLS <yes|no>]` — allow|not allow secure connections (STLS command)

- `SET [secureConnAuthTypes (types)]` — sets types of authentication on secure conn.

- `SET [plainConnAuthTypes (types)]` — sets types of authentication on plain conn.

- `SET [secureConnAllowLogin <yes|no>]` — allow/not allow plain text login on secure conn.

- `SET [plainConnAllowLogin <yes|no>]` — allow/not allow plain text login on plain conn.

- `SET [userdbConnectorType <type>]` — sets the type of the userdb connector

- `SET [userdbConnectorName <name>]` — sets the name of the userdb connector

- `SET [greetingsText <text>]` — sets the greeting text for this service

- `CONFIG AccessControl` — enters the AccessControl context

- `RESET ` — resets the service to the currently active configuration

- `ADD Listener [address] <address>` — adds a listener to the service

- `UPDATE Listener [address] <address>` — updates a listener from the service

- `REMOVE Listener [address] <address>` — removes a listener from the service

- `SHOW Listener [address] <address> [ATTR <name>]` — shows the given listener



## SERVER/POP3-Proxy




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SAVE Config` — saves the server's running configuration

- `LIST Listeners` — lists available listeners

- `START Service` — starts the pop3 proxy service

- `STOP Service` — stops the pop3 proxy service

- `SET [maxErrors <maxErrors>]` — sets max no. of wrong commands

- `SET [maxAuthErrors <maxErrors>]` — sets max no. of failed authentications

- `SET [maxConnThreads <maxThreads>]` — sets max no. of threads handling the conn.

- `SET [minConnThreads <minThreads>]` — sets min no. of threads handling the conn.

- `SET [logLevel <level>]` — sets the service's logging level

- `SET [logType <type>]` — sets the service's logging type

- `SET [logHost <host>]` — sets the service's remote logging host

- `SET [allowStartTLS <yes|no>]` — allow|not allow secure connections (STLS command)

- `SET [userdbConnectorType <type>]` — sets the type of the userdb connector

- `SET [userdbConnectorName <name>]` — sets the name of the userdb connector

- `SET [authenticateOnProxy <yes|no>]` — specifies if user authentication should be done also on proxy

- `SET [greetingsText <text>]` — sets the greeting text for this service

- `RESET ` — resets the service to the currently active configuration

- `CONFIG AccessControl` — enters the AccessControl context

- `CONFIG connectionData` — enters the connection data context

- `CONFIG mappingData` — enters the mapping data context

- `ADD Listener [address] <address>` — adds a listener to the service

- `UPDATE Listener [address] <address>` — updates a listener from the service

- `REMOVE Listener [address] <address>` — removes a listener from the service

- `SHOW Listener [address] <address> [ATTR <name>]` — shows the given listener



## SERVER/POP3-Proxy/AccessControl




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `LIST AllowRules` — lists the allow rules for this listener

- `LIST DenyRules` — lists the deny rules for this listener

- `SET [maxConnections <maxConn>]` — sets max number of connections

- `SET [timeInterval <interval>]` — sets the time interval

- `SET [maxIntervalConnections <interval>]` — sets max connections in time interval

- `SET [peerMaxConnections <maxConn>]` — sets sets max connections no. from a single host

- `SET [peerTimeInterval <interval>]` — sets the time interval - single host

- `SET [peerMaxIntervalConnections <interval>]` — sets max connections in time interval - single host

- `ADD DenyRule [ipSet] <ipRange> [enable <yes|no>] [priority <priority>]` — adds a deny rule to the listener

- `UPDATE DenyRule [ipSet] <ipRange> [enable <yes|no>] [priority <priority>]` — updates a deny rule from the listener

- `REMOVE DenyRule [ipSet] <ipRange>` — removes a deny rule from the listener

- `SHOW DenyRule [ipSet] <ipRange>` — shows the given rule

- `ADD AllowRule [ipSet] <ipRange>` — adds an allow rule to the listener

- `UPDATE AllowRule [ipSet] <ipRange>` — updates an allow rule from the listener

- `REMOVE AllowRule [ipSet] <ipRange>` — removes an allow rule from the listener

- `SHOW AllowRule [ipSet] <ipRange>` — shows the given rule



## SERVER/POP3-Proxy/connectionData




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — switches back to the previous context (does not cancel changes)

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [rwTimeout <no.>]` — sets the timeout for the read/write operation

- `SET [maxConnections <no.>]` — sets the maximum number of simultaneous connections made to AXIGEN backservers

- `SET [sslEnable <yes|no>]` — specifies if the connection should be SSL

- `SET [localInterface <interface>]` — specifies the address of the interface used to make the connections



## SERVER/POP3-Proxy/mappingData




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — switches back to the previous context (does not cancel changes)

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [userMap <map>]` — a userMap from the list defined on the server

- `SET [mappingHost <host>]` — sets the name or IP address of a default AXIGEN machine to be used if userMap is set to none

- `SET [mappingPort <port>]` — sets the port on which to connect to the default AXIGEN machine



## SERVER/POP3/AccessControl




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `LIST AllowRules` — lists the allow rules for this listener

- `LIST DenyRules` — lists the deny rules for this listener

- `SET [maxConnections <maxConn>]` — sets max number of connections

- `SET [timeInterval <interval>]` — sets the time interval

- `SET [maxIntervalConnections <interval>]` — sets max connections in time interval

- `SET [peerMaxConnections <maxConn>]` — sets sets max connections no. from a single host

- `SET [peerTimeInterval <interval>]` — sets the time interval - single host

- `SET [peerMaxIntervalConnections <interval>]` — sets max connections in time interval - single host

- `ADD DenyRule [ipSet] <ipRange> [enable <yes|no>] [priority <priority>]` — adds a deny rule to the listener

- `UPDATE DenyRule [ipSet] <ipRange> [enable <yes|no>] [priority <priority>]` — updates a deny rule from the listener

- `REMOVE DenyRule [ipSet] <ipRange>` — removes a deny rule from the listener

- `SHOW DenyRule [ipSet] <ipRange>` — shows the given rule

- `ADD AllowRule [ipSet] <ipRange>` — adds an allow rule to the listener

- `UPDATE AllowRule [ipSet] <ipRange>` — updates an allow rule from the listener

- `REMOVE AllowRule [ipSet] <ipRange>` — removes an allow rule from the listener

- `SHOW AllowRule [ipSet] <ipRange>` — shows the given rule



## SERVER/PROCESSING




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SAVE Config` — saves the server's running configuration

- `START Service` — starts the processing service

- `STOP Service` — stops the processing service

- `SET [maxSchedInterval <maxInterval>]` — sets max interval for rescheduling a mail

- `SET [schedInterval <interval>]` — sets interval for rescheduling queue checking

- `SET [maxRetryCount <count>]` — sets max no. of times for trying to deliver

- `SET [queuePath <path>]` — sets path to internal server queue

- `SET [queueEntryCount <count>]` — sets upper limit for no. of sub-directories in queue

- `SET [deliveryThreads <threads>]` — sets no. of threads handling SMTP delivery

- `SET [filteringThreads <threads>]` — sets no. of threads handling message filtering

- `SET [logLevel <level>]` — sets the service's logging level

- `SET [logType <type>]` — sets the service's logging type

- `SET [logHost <host>]` — sets the service's remote logging host

- `SET [procQueueSize <size>]` — sets the size of internal processing queue

- `SET [messagesPerSecond <no>]` — sets the maximum number of messages a mail box can receive in one second

- `SET [disableInterval <no>]` — sets the time interval a mail box will be disabled if messagesPerSecond limit is exceeded

- `SET [greylistingCache <no>]` — sets the number of minutes a greylisted entry is kept in cache

- `SHOW Statistics` — shows processing statistical information

- `SHOW SearchIndexJobs` — shows the status of the running mail search index jobs

- `SHOW CalendarSearchIndexJobs` — shows the status of the running calendar search index jobs

- `SHOW ContactSearchIndexJobs` — shows the status of the running contact search index jobs

- `SHOW SortIndexJobs` — shows the status of the running sort index jobs

- `SHOW ConversationIndexJobs` — shows the status of the running conversation index jobs

- `SHOW UserJobStats [detailed]` — shows information about users, scheduled jobs and job statistics

- `RESET ` — resets the service to the currently active configuration



## SERVER/REPORT




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SAVE Config` — saves the server's running configuration

- `LIST Listeners` — lists available listeners

- `LIST SNMPTrapDestinations` — lists available SNMP trap destinations

- `START Service` — starts the report service

- `STOP Service` — stops the report service

- `SET [logLevel <level>]` — sets the service's logging level

- `SET [logType <type>]` — sets the service's logging type

- `SET [logHost <host>]` — sets the service's remote logging host

- `SET [SNMPEnable <yes|no>]` — enables/disables the snmp module

- `SET [SNMPSentTrapsToAllManagers <yes|no>]` — enables/disables sending traps to all managers (including managers not added from configuration)

- `SET [SNMPCommunity <string>]` — sets the SNMP Community string

- `SET [DomainEnable <yes|no>]` — enables/disabled domain level reporting

- `SET [DomainObjectEnable <yes|no>]` — enables/disabled domain object level reporting

- `SET [reportingInterval <weeks>]` — sets the reporting weeks interval

- `ADD Listener [address] <address>` — adds a listener to the service

- `UPDATE Listener [address] <address>` — updates a listener from the service

- `REMOVE Listener [address] <address>` — removes a listener from the service

- `SHOW Listener [address] <address> [ATTR <param>]` — shows the given listener

- `ADD SNMPTrapDestination <address>` — adds a snmp trap destination to the service

- `REMOVE SNMPTrapDestination <address>` — removes a snmp trap destination from the service

- `RESET ` — resets the service to the currently active configuration



## SERVER/RPOP




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SAVE Config` — saves the server's running configuration

- `START Service` — starts the rpop service

- `STOP Service` — stops the rpop service

- `SET [maxConnThreads <maxThreads>]` — sets max no. of threads handling the conn.

- `SET [minConnThreads <minThreads>]` — sets min no. of threads handling the conn.

- `SET [logLevel <level>]` — sets the service's logging level

- `SET [logType <type>]` — sets the service's logging type

- `SET [logHost <host>]` — sets the service's remote logging host

- `RESET ` — resets the service to the currently active configuration



## SERVER/SECURITY




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SAVE Config` — saves the server's running configuration

- `SET [logLevel <level>]` — sets the service's logging level

- `SET [logType <type>]` — sets the service's logging type

- `SET [logHost <host>]` — sets the service's remote logging host

- `RESET ` — resets the service to the currently active configuration



## SERVER/SMTP-INCOMING




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SAVE Config` — saves the server's running configuration

- `LIST Listeners` — lists available listeners

- `START Service` — starts the smtp incoming service

- `STOP Service` — stops the smtp incoming service

- `SET [maxErrors <maxErrors>]` — sets max no. of wrong commands

- `SET [maxAuthErrors <maxErrors>]` — sets max no. of failed authentications

- `SET [maxConnThreads <maxThreads>]` — sets max no. of threads handling the conn.

- `SET [minConnThreads <minThreads>]` — sets min no. of threads handling the conn.

- `SET [logLevel <level>]` — sets the service's logging level

- `SET [logType <type>]` — sets the service's logging type

- `SET [logHost <host>]` — sets the service's remote logging host

- `SET [maxReceivedHeaders <maxHeaders>]` — sets max no. of received headers for a mail

- `SET [userdbConnectorType <type>]` — sets the type of the userdb connector

- `SET [userdbConnectorName <name>]` — sets the name of the userdb connector

- `SET [enableSmtpRouting <yes|no>]` — allow this service to become a routing smtp service

- `RESET ` — resets the service to the currently active configuration

- `CONFIG mappingData` — enters the mapping data context

- `CONFIG AccessControl` — enters the AccessControl context

- `ADD Listener [address] <address>` — adds a listener to the service

- `UPDATE Listener [address] <address>` — updates a listener from the service

- `REMOVE Listener [address] <address>` — removes a listener from the service

- `SHOW Listener [address] <address> [ATTR <param>]` — shows the given listener



## SERVER/SMTP-INCOMING/AccessControl




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `LIST AllowRules` — lists the allow rules for this listener

- `LIST DenyRules` — lists the deny rules for this listener

- `SET [maxConnections <maxConn>]` — sets max number of connections

- `SET [timeInterval <interval>]` — sets the time interval

- `SET [maxIntervalConnections <interval>]` — sets max connections in time interval

- `SET [peerMaxConnections <maxConn>]` — sets sets max connections no. from a single host

- `SET [peerTimeInterval <interval>]` — sets the time interval - single host

- `SET [peerMaxIntervalConnections <interval>]` — sets max connections in time interval - single host

- `ADD DenyRule [ipSet] <ipRange> [enable <yes|no>] [priority <priority>]` — adds a deny rule to the listener

- `UPDATE DenyRule [ipSet] <ipRange> [enable <yes|no>] [priority <priority>]` — updates a deny rule from the listener

- `REMOVE DenyRule [ipSet] <ipRange>` — removes a deny rule from the listener

- `SHOW DenyRule [ipSet] <ipRange>` — shows the given rule

- `ADD AllowRule [ipSet] <ipRange>` — adds an allow rule to the listener

- `UPDATE AllowRule [ipSet] <ipRange>` — updates an allow rule from the listener

- `REMOVE AllowRule [ipSet] <ipRange>` — removes an allow rule from the listener

- `SHOW AllowRule [ipSet] <ipRange>` — shows the given rule



## SERVER/SMTP-INCOMING/mappingData




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — switches back to the previous context (does not cancel changes)

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [userMap <map>]` — a userMap from the list defined on the server

- `SET [mappingHost <host>]` — sets the name or IP address of a default AXIGEN machine to be used if userMap is set to none

- `SET [mappingPort <port>]` — sets the port on which to connect to the default AXIGEN machine



## SERVER/SMTP-OUTGOING




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SAVE Config` — saves the server's running configuration

- `START Service` — starts the smtp outgoing service

- `STOP Service` — stops the smtp outgoing service

- `SET [enableIPv6 <yes|no>]` — enables or disables IPv6 networking in the smtp outgoing service

- `SET [maxConnThreads <maxThreads>]` — sets max no. of threads handling the conn.

- `SET [minConnThreads <minThreads>]` — sets min no. of threads handling the conn.

- `SET [logLevel <level>]` — sets the service's logging level

- `SET [logType <type>]` — sets the service's logging type

- `SET [logHost <host>]` — sets the service's remote logging host

- `RESET ` — resets the service to the currently active configuration



## SERVER/SRVLOG




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SAVE Config` — saves the server's running configuration

- `SET [logLevel <level>]` — sets the service's logging level

- `SET [logType <type>]` — sets the service's logging type

- `SET [logHost <host>]` — sets the service's remote logging host

- `RESET ` — resets the service to the currently active configuration



## SERVER/USERDB




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `LIST ldapConnectors` — lists the ldap connectors

- `SET [logLevel <level>]` — sets the service's logging level

- `SET [logType <type>]` — sets the service's logging type

- `SET [logHost <host>]` — sets the service's remote logging host

- `SET [maxThreads <no.>]` — sets the maximum number of processing threads

- `RESET ` — resets the service to the currently active configuration

- `ADD ldapConnector [name] <name> ldapUri <uri>` — adds a ldap connector to the service

- `UPDATE ldapConnector [name] <name>` — updates a ldap connector from the service

- `REMOVE ldapConnector [name] <name>` — removes a ldap connector from the service

- `SHOW ldapConnector [name] <name> [ATTR <param>]` — shows the given ldap connector

- `ADD oauthConnector name <name> mode <oidc|oauth2>` — add a new OAuth connector

- `LIST oauthConnectors` — list all OAuth connectors

- `UPDATE oauthConnector [name] <name>` — updates an OAuth connector

- `SHOW oauthConnector [name] <name> [[ATTR] <param>]` — shows the given OAuth connector

- `SET defaultOAuthConnector [name] <name>` — Sets the default OAuth connector

- `REMOVE oauthConnector [name] <name>` — Remove the named connector

- `RESET defaultZoomConnector` — Create the default Zoom.us connector or reset the existing one

- `RESET defaultTeamsConnector` — Create the default Microsoft Teams connector or reset the existing one



## SERVER/USERDB/ldapConnector




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [name <name>]` — sets the Ldap connector name.

- `SET [bindDN <str>]` — sets the distinguished name for binding

- `SET [bindPass <str>]` — sets the password for binding

- `SET [axigenHostField <field>]` — sets the name of the field containing the axigen server hostname

- `SET [ldapURI1 <uri>]` — sets the first URI to use

- `SET [ldapURI2 <uri>]` — sets the second URI to use

- `SET [ldapURI3 <uri>]` — sets the third URI to use

- `SET [ldapURI4 <uri>]` — sets the fourth URI to use

- `SET [ldapURI5 <uri>]` — sets the fifth URI to use

- `SET [synchronizationDirection <choice>]` — values: axigenToLdap | ldapToAxigen | bothWays

- `SET [synchronizationConflictResolution <choice>]` — values: axigenWins | ldapWins | noChange

- `SET [serverType <choice>]` — values: OpenLdap | ActiveDirectory

- `SET [timeout <no>]` — sets the connection timeout

- `SET [accountBaseDN <DN>]` — sets the account base DN

- `SET [groupBaseDN <DN>]` — sets the group base DN

- `SET [useCustomSchema <yes|no>]` — enables/disables usage of a custom schema

- `SET [customSchemaFile <path>]` — sets the custom schema file path

- `SET [pollingInterval <no.>]` — sets polling interval

- `SET [transientErrorRetryInterval <no.>]` — sets the interval in seconds between retries on operations with transient errors

- `SET [clusteredSetup <yes|no>]` — enables/disables clustered setup

- `SET [searchDomainAliases <yes|no>]` — enables/disables domain aliases ldap search

- `SET [ignoreLDAPDeletes <yes|no>]` — enables/disables the LDAP deletes to be synchronized in axigen

- `SET [replicaId <number>]` — sets id of replica (0-999); must be unique between axigen servers



## SERVER/USERDB/oauthConnector




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET clientId <value>` — Client ID

- `SET clientSecret <value>` — Client Secret (password)

- `SET autoConfigUri <value>` — Autoconfig URL (OIDC only)

- `SET jwksUri <value>` — JWKS Urls for RSA keys (OAuth 2.0)

- `SET authzUri <value>` — Authorization endpoint (for redirects)

- `SET tokenUri <value>` — Token Exchange URI

- `SET introspectUri <value>` — Introspection URI (OAuth 2 only)

- `SET usernameField <value>` — Username field

- `SET usernamePrefix <value>` — Username prefix

- `SET clientScopes <value>` — String to use for client token bearer scope

- `SET defaultTokenExpiry <value>` — Default expiration time for OAuth token (unless otherwise specified)

- `SET connectTimeout <value>` — Number of seconds to wait for connection to OAuth server to be established

- `SET requestTimeout <value>` — Number of seconds to wait for OAuth request to complete (includes connectionTimeout)

- `SET endpointsBaseUrl <value>` — Base URL at which to access endpoints for a OAuth connected external app

- `SET redirectBaseUrl <value>` — Base URL at which the authorization server redirects the client



## SERVER/Usermap




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [name <name>]` — sets the name of this usermap

- `SET [type <type>]` — sets the type of the usermap

- `SET [userdbConnectorType <type>]` — sets the type of the userdb connector

- `SET [userdbConnectorName <name>]` — sets the name of the userdb connector

- `SET [localFile <path>]` — sets the path to the file containing local mapping



## SERVER/WEBADMIN




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SAVE Config` — saves the server's running configuration

- `LIST Listeners` — lists available listeners

- `LIST UrlRedirects` — lists the rules used for secure login

- `START Service` — starts the webadmin service

- `STOP Service` — stops the webadmin service

- `SET [maxErrors <maxErrors>]` — sets max no. of wrong commands

- `SET [maxAuthErrors <maxErrors>]` — sets max no. of failed authentications

- `SET [maxConnThreads <maxThreads>]` — sets max no. of threads handling the conn.

- `SET [minConnThreads <minThreads>]` — sets min no. of threads handling the conn.

- `SET [logLevel <level>]` — sets the service's logging level

- `SET [logType <type>]` — sets the service's logging type

- `SET [logHost <host>]` — sets the service's remote logging host

- `SET [path <path>]` — sets the location of HSP files

- `SET [sessionIdleTimeout <timeout>]` — sets the inactivity timeout

- `SET [sessionActivityTimeout <timeout>]` — sets maximum living time for a session

- `SET [allowKeepAlive <yes|no>]` — enables/disables persistent connection

- `SET [allowLargeIncomingData <yes|no>]` — enables/disables receiving incoming data after the limit is exceeded

- `SET [httpHeadersMaxSize <size>]` — sets the maximum allowed size for received HTTP headers

- `SET [httpBodyMaxSize <size>]` — sets the maximum allowed size for incoming HTTP body

- `SET [httpServerHeaderEnable <yes|no>]` — enables/disables sending the Server header on HTTP responses

- `SET [httpHstsHeaderValue <value>]` — sets the value of the Strict-Transport-Security HTTP response header

- `SET [uploadMaxSize <size>]` — sets the maximum allowed size for incoming upload data

- `SET accountSecurityAlternativeEmailAddressEnabled <yes|no>` — enables/disables the use of an alternative email address for account security

- `SET accountSecurityPhoneNumberEnabled <yes|no>` — enables/disables the use of a phone number for account security

- `SET accountSecuritySmsConnector <smsConnectorName>` — configures the SMS Connector to be used for sending SMS to the configured phone number

- `SET accountSecurityMandatory <yes|no>` — enforces the end-user configuration of the account security methods

- `SET accountSecurityUpdateInterval <days>` — sets the time interval (in days) after which the account security update dialog is displayed to the end-user

- `SET twoFactorAuthEnabled <disabled|enabled|mandatory>` — enables/disables two factor authentication

- `SET twoFactorAuthCommunicationMethods ([email] [sms] [authApp])` — sets the communication methods available for two factor authentication

- `SET twoFactorAuthEmailFileName <path>` — name of the file containing the email message template sent to the user's alternative email address for two factor authentication

- `SET twoFactorAuthSmsFileName <path>` — name of the file containing the SMS message template sent to the user's phone number for two factor authentication

- `CONFIG AccessControl` — enters the AccessControl context

- `RESET ` — resets the service to the currently active configuration

- `ADD Listener [address] <address>` — adds a listener to the service

- `UPDATE Listener [address] <address>` — updates a listener from the service

- `REMOVE Listener [address] <address>` — removes a listener from the service

- `SHOW Listener [address] <address> [ATTR <param>]` — shows the given listener

- `ADD UrlRedirect [address] <address> port <port> host <host> [auto <yes|no>]` — 

- `UPDATE UrlRedirect [address] <address> [port <port>] [host <host>] [auto <yes|no>]` — 

- `REMOVE UrlRedirect [address] <address>` — 



## SERVER/WEBADMIN/AccessControl




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `LIST AllowRules` — lists the allow rules for this listener

- `LIST DenyRules` — lists the deny rules for this listener

- `SET [maxConnections <maxConn>]` — sets max number of connections

- `SET [timeInterval <interval>]` — sets the time interval

- `SET [maxIntervalConnections <interval>]` — sets max connections in time interval

- `SET [peerMaxConnections <maxConn>]` — sets sets max connections no. from a single host

- `SET [peerTimeInterval <interval>]` — sets the time interval - single host

- `SET [peerMaxIntervalConnections <interval>]` — sets max connections in time interval - single host

- `ADD DenyRule [ipSet] <ipRange> [enable <yes|no>] [priority <priority>]` — adds a deny rule to the listener

- `UPDATE DenyRule [ipSet] <ipRange> [enable <yes|no>] [priority <priority>]` — updates a deny rule from the listener

- `REMOVE DenyRule [ipSet] <ipRange>` — removes a deny rule from the listener

- `SHOW DenyRule [ipSet] <ipRange>` — shows the given rule

- `ADD AllowRule [ipSet] <ipRange>` — adds an allow rule to the listener

- `UPDATE AllowRule [ipSet] <ipRange>` — updates an allow rule from the listener

- `REMOVE AllowRule [ipSet] <ipRange>` — removes an allow rule from the listener

- `SHOW AllowRule [ipSet] <ipRange>` — shows the given rule



## SERVER/WEBMAIL




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SAVE Config` — saves the server's running configuration

- `LIST Listeners` — lists available listeners

- `LIST UrlRedirects` — lists the rules used for secure login

- `LIST HostNameResolvers` — lists the hostname resolvers

- `START Service` — starts the webmail service

- `STOP Service` — stops the webmail service

- `SET [maxErrors <maxErrors>]` — sets max no. of wrong commands

- `SET [maxAuthErrors <maxErrors>]` — sets max no. of failed authentications

- `SET [maxConnThreads <maxThreads>]` — sets max no. of threads handling the conn.

- `SET [minConnThreads <minThreads>]` — sets min no. of threads handling the conn.

- `SET [logLevel <level>]` — sets the service's logging level

- `SET [logType <type>]` — sets the service's logging type

- `SET [logHost <host>]` — sets the service's remote logging host

- `SET [path <path>]` — sets the location of HSP files

- `SET [sessionIdleTimeout <timeout>]` — sets the inactivity timeout

- `SET [sessionActivityTimeout <timeout>]` — sets maximum living time for a session

- `SET [allowKeepAlive <yes|no>]` — enables/disables persistent connection

- `SET [allowLargeIncomingData <yes|no>]` — enables/disables receiving incoming data after the limit is exceeded

- `SET [httpHeadersMaxSize <size>]` — sets the maximum allowed size for received HTTP headers

- `SET [httpBodyMaxSize <size>]` — sets the maximum allowed size for incoming HTTP body

- `SET [httpServerHeaderEnable <yes|no>]` — enables/disables sending the Server header on HTTP responses

- `SET [httpHstsHeaderValue <value>]` — sets the value of the Strict-Transport-Security HTTP response header

- `SET [uploadMaxSize <size>]` — sets the maximum allowed size for incoming upload data

- `SET [showDomainList <yes|no>]` — enables/disables displaying domains list at user login

- `SET [userdbConnectorType <type>]` — sets the type of the userdb connector

- `SET [userdbConnectorName <name>]` — sets the name of the userdb connector

- `SET [enableMobileWebmail <yes|no>]` — enables/disables mobile webmail

- `SET [enableActiveSync <yes|no>]` — enables/disables activeSync

- `SET [enableIcalCalendar <yes|no>]` — enables/disables Calendar (ICS) access through iCal/HTTP

- `SET [enableIcalFreebusy <yes|no>]` — enables/disables Free/Busy (IFB) access through iCal/HTTP

- `SET [enableWebDAVCardDAV <yes|no>]` — enables/disables WebDAVCardDAV access through WebDAV/HTTP

- `SET [enableWebDAVCalDAV <yes|no>]` — enables/disables WebDAVCalDAV access through WebDAV/HTTP

- `SET [userInterfaceType <ajaxDefault | ajaxOnly | standardDefault | standardOnly>]` — 

- `SET [enablePasswordRecovery <yes|no>]` — enables/disables password recovery at server level

- `SET [enableUsernameRecovery <yes|no>]` — enables/disables username recovery at server level

- `SET [allowSPNEGOAuth <yes|no>` — allow/deny single sign on authentication using SPNEGO

- `SET [enableLoginCaptcha <yes|no>` — allow/deny captcha validation on login page

- `SET [showCaptchaAfterFailedLoginsCount <count>` — sets the number of failed logins after which the captcha is displayed on login page

- `SET [enableZoomConnector <yes|no>]` — enables/disables the Zoom connector

- `SET [enableTeamsConnector <yes|no>]` — enables/disables the Teams connector

- `SET [enableOfficeDocumentsPreview <yes|no>` — enables/disables the preview of Office documents

- `SET [batchAsyncThreshold <count>` — time threshold in milliseconds to wait for batch jobs to finish in order to respond synchronously to requests

- `SET [accessControlAllowOrigin <none | * | origin>]` — sets the CORS allowed origin for the native API endpoints

- `CONFIG AccessControl` — enters the AccessControl context

- `RESET ` — resets the service to the currently active configuration

- `ADD Listener [address] <address>` — adds a listener to the service

- `UPDATE Listener [address] <address>` — updates a listener from the service

- `REMOVE Listener [address] <address>` — removes a listener from the service

- `SHOW Listener [address] <address> [ATTR <param>]` — shows the given listener

- `ADD HostNameResolver [host] <host> [domain <domain>]` — adds a host name (WebMail URL) to HSP template name mapping

- `UPDATE HostNameResolver [host] <host> [domain <domain>]` — updates a host name (WebMail URL) to HSP template name mapping

- `REMOVE HostNameResolver [host] <host>` — removes a host name (WebMail URL) to HSP template name mapping

- `SHOW HostNameResolver [host] <host>` — shows a virtual host configuration *The domain parameter refers to the HSP template directory

- `ADD UrlRedirect [address] <address> port <port> host <host> [auto <yes|no>]` — 

- `UPDATE UrlRedirect [address] <address> [port <port>] [host <host>] [auto <yes|no>]` — 

- `REMOVE UrlRedirect [address] <address>` — 



## SERVER/WEBMAIL-Proxy




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SAVE Config` — saves the server's running configuration

- `LIST Listeners` — lists available listeners

- `LIST UrlRedirects` — lists the rules used for secure login

- `LIST HostNameResolvers` — lists the hostname resolvers

- `START Service` — starts the webmail service

- `STOP Service` — stops the webmail service

- `SET [maxErrors <maxErrors>]` — sets max no. of wrong commands

- `SET [maxAuthErrors <maxErrors>]` — sets max no. of failed authentications

- `SET [maxConnThreads <maxThreads>]` — sets max no. of threads handling the conn.

- `SET [minConnThreads <minThreads>]` — sets min no. of threads handling the conn.

- `SET [logLevel <level>]` — sets the service's logging level

- `SET [logType <type>]` — sets the service's logging type

- `SET [logHost <host>]` — sets the service's remote logging host

- `SET [path <path>]` — sets the location of HSP files

- `SET [allowKeepAlive <yes|no>]` — enables/disables persistent connection

- `SET [allowLargeIncomingData <yes|no>]` — enables/disables receiving incoming data after the limit is exceeded

- `SET [httpHeadersMaxSize <size>]` — sets the maximum allowed size for received HTTP headers

- `SET [httpBodyMaxSize <size>]` — sets the maximum allowed size for incoming HTTP body

- `SET [httpServerHeaderEnable <yes|no>]` — enables/disables sending the Server header on HTTP responses

- `SET [httpHstsHeaderValue <value>]` — sets the value of the Strict-Transport-Security HTTP response header

- `SET [userdbConnectorType <type>]` — sets the type of the userdb connector

- `SET [userdbConnectorName <name>]` — sets the name of the userdb connector

- `SET [requestsQueueMaxSize <size>]` — sets the maximum number of queued requests/backend

- `SET [authenticateOnProxy <yes|no>]` — enables/disables authentication on proxy

- `SET [enableMobileWebmail <yes|no>]` — enables/disables mobile webmail

- `SET [userInterfaceType <ajaxDefault | ajaxOnly | standardDefault | standardOnly>]` — 

- `SET [httpBindBackend <url>]` — sets the http url of the IM backend

- `SET [enablePasswordRecovery <yes|no>]` — enables/disables password recovery at server level

- `SET [enableUsernameRecovery <yes|no>]` — enables/disables username recovery at server level

- `SET [allowSPNEGOAuth <yes|no>` — allow/deny single sign on authentication using SPNEGO

- `SET [enableLoginCaptcha <yes|no>` — allow/deny captcha validation on login page

- `SET [showCaptchaAfterFailedLoginsCount <count>` — sets the number of failed logins after which the captcha is displayed on login page

- `SET [accessControlAllowOrigin <none | * | origin>]` — sets the CORS allowed origin for the native API endpoints

- `CONFIG AccessControl` — enters the AccessControl context

- `CONFIG ConnectionData` — enters the ConnectionData context

- `CONFIG MappingData` — enters the MappingData context

- `RESET ` — resets the service to the currently active configuration

- `ADD Listener [address] <address>` — adds a listener to the service

- `UPDATE Listener [address] <address>` — updates a listener from the service

- `REMOVE Listener [address] <address>` — removes a listener from the service

- `SHOW Listener [address] <address> [ATTR <param>]` — shows the given listener

- `ADD HostNameResolver [host] <host> [domain <domain>]` — adds a host name (WebMail URL) to HSP template name mapping

- `UPDATE HostNameResolver [host] <host> [domain <domain>]` — updates a host name (WebMail URL) to HSP template name mapping

- `REMOVE HostNameResolver [host] <host>` — removes a host name (WebMail URL) to HSP template name mapping

- `SHOW HostNameResolver [host] <host>` — shows a virtual host configuration *The domain parameter refers to the HSP template directory

- `ADD UrlRedirect [address] <address> port <port> host <host> [auto <yes|no>]` — 

- `UPDATE UrlRedirect [address] <address> [port <port>] [host <host>] [auto <yes|no>]` — 

- `REMOVE UrlRedirect [address] <address>` — 



## SERVER/WEBMAIL-Proxy/AccessControl




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `LIST AllowRules` — lists the allow rules for this listener

- `LIST DenyRules` — lists the deny rules for this listener

- `SET [maxConnections <maxConn>]` — sets max number of connections

- `SET [timeInterval <interval>]` — sets the time interval

- `SET [maxIntervalConnections <interval>]` — sets max connections in time interval

- `SET [peerMaxConnections <maxConn>]` — sets sets max connections no. from a single host

- `SET [peerTimeInterval <interval>]` — sets the time interval - single host

- `SET [peerMaxIntervalConnections <interval>]` — sets max connections in time interval - single host

- `ADD DenyRule [ipSet] <ipRange> [enable <yes|no>] [priority <priority>]` — adds a deny rule to the listener

- `UPDATE DenyRule [ipSet] <ipRange> [enable <yes|no>] [priority <priority>]` — updates a deny rule from the listener

- `REMOVE DenyRule [ipSet] <ipRange>` — removes a deny rule from the listener

- `SHOW DenyRule [ipSet] <ipRange>` — shows the given rule

- `ADD AllowRule [ipSet] <ipRange>` — adds an allow rule to the listener

- `UPDATE AllowRule [ipSet] <ipRange>` — updates an allow rule from the listener

- `REMOVE AllowRule [ipSet] <ipRange>` — removes an allow rule from the listener

- `SHOW AllowRule [ipSet] <ipRange>` — shows the given rule



## SERVER/WEBMAIL-Proxy/ConnectionData




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — switches back to the previous context (does not cancel changes)

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [rwTimeout <no.>]` — sets the timeout for the read/write operation

- `SET [maxConnections <no.>]` — sets the maximum number of simultaneous connections made to AXIGEN backservers

- `SET [sslEnable <yes|no>]` — specifies if the connection should be SSL

- `SET [localInterface <interface>]` — specifies the address of the interface used to make the connections



## SERVER/WEBMAIL-Proxy/MappingData




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — switches back to the previous context (does not cancel changes)

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [userMap <map>]` — a userMap from the list defined on the server

- `SET [mappingHost <host>]` — sets the name or IP address of a default AXIGEN machine to be used if userMap is set to none

- `SET [mappingPort <port>]` — sets the port on which to connect to the default AXIGEN machine



## SERVER/WEBMAIL/AccessControl




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `LIST AllowRules` — lists the allow rules for this listener

- `LIST DenyRules` — lists the deny rules for this listener

- `SET [maxConnections <maxConn>]` — sets max number of connections

- `SET [timeInterval <interval>]` — sets the time interval

- `SET [maxIntervalConnections <interval>]` — sets max connections in time interval

- `SET [peerMaxConnections <maxConn>]` — sets sets max connections no. from a single host

- `SET [peerTimeInterval <interval>]` — sets the time interval - single host

- `SET [peerMaxIntervalConnections <interval>]` — sets max connections in time interval - single host

- `ADD DenyRule [ipSet] <ipRange> [enable <yes|no>] [priority <priority>]` — adds a deny rule to the listener

- `UPDATE DenyRule [ipSet] <ipRange> [enable <yes|no>] [priority <priority>]` — updates a deny rule from the listener

- `REMOVE DenyRule [ipSet] <ipRange>` — removes a deny rule from the listener

- `SHOW DenyRule [ipSet] <ipRange>` — shows the given rule

- `ADD AllowRule [ipSet] <ipRange>` — adds an allow rule to the listener

- `UPDATE AllowRule [ipSet] <ipRange>` — updates an allow rule from the listener

- `REMOVE AllowRule [ipSet] <ipRange>` — removes an allow rule from the listener

- `SHOW AllowRule [ipSet] <ipRange>` — shows the given rule



## SERVER/smsConnector




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET url <value>` — URL for send request

- `SET method <value>` — HTTP method for send request

- `SET contentType <value>` — Content type for send request (none|json|formUrlEncoded)

- `SET toParamName <value>` — Name of parameter containing the recipient of the message

- `SET bodyParamName <value>` — Name of parameter containing the text of the message

- `SET fromParamName <value>` — Name of the parameter containing the 'From' text

- `CONFIG Auth` — Enters authorization configuration context

- `ADD staticParam <name> <value>` — Adds a static parameter (gets added to the request)

- `UPDATE staticParam <name> <value>` — Updates the value of the static parameter

- `LIST staticParams` — Lists all static parameters

- `REMOVE staticParam <name>` — Removes the named static parameter



## SERVER/smsConnector/Auth




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET type <value>` — HTTP Authorization type (none|basic|bearer)

- `SET username <value>` — Username (for Basic authentication)

- `SET password <value>` — Password (for Basic authentication)

- `SET token <value>` — Token (for Bearer authentication)



## TRACER




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — switches back to the previous context

- `ENABLE WEBDAV TRACE FOR USER <user@domain> INTO <file>` — enable webdav tracing for an user

- `DISABLE WEBDAV TRACE` — disable webdav tracing

- `ENABLE HTTPC TRACE FOR <label> INTO <file> [MODE PROTOCOL|HEX]` — Enable httpc client tracing (special labels: * for all, none for none)

- `DISABLE HTTPC TRACE` — Disable httpc client tracing

- `ENABLE CALENDAR AUDIT FOR USER <regex> INTO CALLOG|FILE <file>` — Enable calendar audit for one or multiple users

- `DISABLE CALENDAR AUDIT` — Disable calendar audit

- `DECODE CIPHERSUITE <ciphers> [legacy]` — Provides a human readable representation for a hex string of cipher/cipher suite



## aacl/admin-group




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW ` — shows information about this context

- `LIST parents` — lists all group's parents

- `LIST members` — lists all group's members

- `SET name <name>` — sets group's name

- `SET description <desc>` — sets group's description

- `ADD parent-group [name] <name>` — adds a new parent group

- `REMOVE parent-group [name] <name>` — removes a parent group

- `GRANT permission (<permNames>) [domain <name>]` — grants permissions on server or a domain for group

- `REVOKE permission (<permNames>) [domain <name>]` — revokes permissions on server or a domain for group

- `DENY permission (<permNames>) [domain <name>]` — denyes permissions on server or a domain for group

- `SHOW effective-permissions [domain <name>]` — shows group's effective permissions on server or a domain permissions:  - manageServerConfig manageServerFilters manageCluster manageProcessing manageLog manageDNR manageSMTPIn manageSMTPOut managePOP3 manageIMAP manageWebMail manageRPOP managePOP3Proxy manageIMAPProxy manageWebmailProxy manageCLI manageWebAdmin manageFTPBackup manageReporting accessDumpData manageAuthentication activateAnyDomain manageConfigOnAnyDomain manageFiltersOnAnyDomain backupAnyDomain restoreAnyDomain deactivateAnyDomain manageAdminLimitsOnAnyDomain manageServicesOnAnyDomain manageCatchAllOnAnyDomain manageGroupwareOnAnyDomain manageLdapSyncOnAnyDomain manageDomainAliasesOnAnyDomain manageDomainStorageOnAnyDomain manageAccountServicesOnAnyDomain manageAutomaticMigrationOnAnyDomain manageFoldersQuotasOnAnyDomain managePasswordPolicyOnAnyDomain manageWebmailLimitsOnAnyDomain manageFilteredEmailOnAnyDomain manageSendReceiveRestrictionsOnAnyDomain manageRPOPRestrictionsOnAnyDomain manageTemporaryAddressesOnAnyDomain manageAccountRecoveryOnAnyDomain managePersonalOrganizerOnAnyDomain manageSharingOnAnyDomain manageOutlookConnectorOnAnyDomain manageActiveSyncOnAnyDomain manageIAOnAnyDomain manageAccountsOnAnyDomain createAccountsOnAnyDomain removeAccountsOnAnyDomain manageAccountsNamingOnAnyDomain changeAccountsPasswordOnAnyDomain changeAccountsClassOnAnyDomain manageAccountsContactInformationOnAnyDomain manageAccountsWebmailOptionsOnAnyDomain manageGroupsOnAnyDomain createGroupsOnAnyDomain removeGroupsOnAnyDomain manageGroupsNamingOnAnyDomain manageGroupsMembersOnAnyDomain manageMaillistsOnAnyDomain createMailListsOnAnyDomain removeMailListsOnAnyDomain manageMailListsNamingOnAnyDomain changeMailListsPasswordOnAnyDomain manageMailListsMemberOnAnyDomain manageMailListsSubscriptionOnAnyDomain manageMailListsPostingOnAnyDomain manageMailListsMessageHeadersOnAnyDomain manageMailListsTemplatesOnAnyDomain manageMailListsWebmailOptionsOnAnyDomain manageMailListsServicesOnAnyDomain manageMailListsFoldersQuotasOnAnyDomain manageMailListsWebmailLimitsOnAnyDomain manageMailListsSendReceiveRestrictionsOnAnyDomain manageAccountClassesOnAnyDomain createAccountClassesOnAnyDomain removeAccountClassesOnAnyDomain renameAccountClassesOnAnyDomain manageFolderRecipientsOnAnyDomain managePublicFolderOnAnyDomain createPublicFolderOnAnyDomain removePublicFolderOnAnyDomain renamePublicFolderOnAnyDomain managePublicFoldersQuotasOnAnyDomain manageAdminACL permissions:  - manageSubdomains manageDomainConfig manageDomainFilters backupDomain restoreDomain deactivateDomain manageDomainAdminLimits manageDomainServices manageCatchAll manageGroupware manageLdapSync manageDomainAliases manageDomainStorage manageAccountServices manageAutomaticMigration manageFoldersQuotas managePasswordPolicy manageWebmailLimits manageFilteredEmail manageSendReceiveRestrictions manageRPOPRestrictions manageTemporaryAddresses manageAccountRecovery managePersonalOrganizer manageSharing manageOutlookConnector manageActiveSync manageIA manageAccounts createAccounts removeAccounts manageAccountsNaming changeAccountsPassword changeAccountsClass manageAccountsContactInformation manageAccountsWebmailOptions manageGroups createGroups removeGroups manageGroupsNaming manageGroupsMembers manageMaillists createMailLists removeMailLists manageMailListsNaming changeMailListsPassword manageMailListsMembers manageMailListsSubscription manageMailListsPosting manageMailListsMessageHeaders manageMailListsTemplates manageMailListsWebmailOptions manageMailListsServices manageMailListsFoldersQuotas manageMailListsWebmailLimits manageMailListsSendReceiveRestrictions manageAccountClasses createAccountClasses removeAccountClasses renameAccountClasses manageFolderRecipients managePublicFolder createPublicFolder removePublicFolder renamePublicFolder managePublicFoldersQuotas



## aacl/admin-user




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW ` — shows information about this context

- `LIST parents` — lists all group's parents

- `SET name <name>` — set user's name

- `SET description <desc>` — set user's description

- `SET password <pass>` — set user's password

- `SET twoFactorConfigured <yes|no>` — set user's TwoFactor configuration status

- `ADD parent-group [name] <name>` — adds a new parent group

- `REMOVE parent-group [name] <name>` — removes a parent group

- `GRANT permission (<permNames>) [domain <name>]` — grants permissions on server or a domain for user

- `REVOKE permission (<permNames>) [domain <name>]` — revokes permissions on server or a domain for user

- `DENY permission (<permNames>) [domain <name>]` — denies permissions on server or a domain for user

- `SHOW effective-permissions [domain <name>]` — shows user's effective permissions on server or a domain permissions:  - manageServerConfig manageServerFilters manageCluster manageProcessing manageLog manageDNR manageSMTPIn manageSMTPOut managePOP3 manageIMAP manageWebMail manageRPOP managePOP3Proxy manageIMAPProxy manageWebmailProxy manageCLI manageWebAdmin manageFTPBackup manageReporting accessDumpData manageAuthentication activateAnyDomain manageConfigOnAnyDomain manageFiltersOnAnyDomain backupAnyDomain restoreAnyDomain deactivateAnyDomain manageAdminLimitsOnAnyDomain manageServicesOnAnyDomain manageCatchAllOnAnyDomain manageGroupwareOnAnyDomain manageLdapSyncOnAnyDomain manageDomainAliasesOnAnyDomain manageDomainStorageOnAnyDomain manageAccountServicesOnAnyDomain manageAutomaticMigrationOnAnyDomain manageFoldersQuotasOnAnyDomain managePasswordPolicyOnAnyDomain manageWebmailLimitsOnAnyDomain manageFilteredEmailOnAnyDomain manageSendReceiveRestrictionsOnAnyDomain manageRPOPRestrictionsOnAnyDomain manageTemporaryAddressesOnAnyDomain manageAccountRecoveryOnAnyDomain managePersonalOrganizerOnAnyDomain manageSharingOnAnyDomain manageOutlookConnectorOnAnyDomain manageActiveSyncOnAnyDomain manageIAOnAnyDomain manageAccountsOnAnyDomain createAccountsOnAnyDomain removeAccountsOnAnyDomain manageAccountsNamingOnAnyDomain changeAccountsPasswordOnAnyDomain changeAccountsClassOnAnyDomain manageAccountsContactInformationOnAnyDomain manageAccountsWebmailOptionsOnAnyDomain manageGroupsOnAnyDomain createGroupsOnAnyDomain removeGroupsOnAnyDomain manageGroupsNamingOnAnyDomain manageGroupsMembersOnAnyDomain manageMaillistsOnAnyDomain createMailListsOnAnyDomain removeMailListsOnAnyDomain manageMailListsNamingOnAnyDomain changeMailListsPasswordOnAnyDomain manageMailListsMemberOnAnyDomain manageMailListsSubscriptionOnAnyDomain manageMailListsPostingOnAnyDomain manageMailListsMessageHeadersOnAnyDomain manageMailListsTemplatesOnAnyDomain manageMailListsWebmailOptionsOnAnyDomain manageMailListsServicesOnAnyDomain manageMailListsFoldersQuotasOnAnyDomain manageMailListsWebmailLimitsOnAnyDomain manageMailListsSendReceiveRestrictionsOnAnyDomain manageAccountClassesOnAnyDomain createAccountClassesOnAnyDomain removeAccountClassesOnAnyDomain renameAccountClassesOnAnyDomain manageFolderRecipientsOnAnyDomain managePublicFolderOnAnyDomain createPublicFolderOnAnyDomain removePublicFolderOnAnyDomain renamePublicFolderOnAnyDomain managePublicFoldersQuotasOnAnyDomain manageAdminACL permissions:  - manageSubdomains manageDomainConfig manageDomainFilters backupDomain restoreDomain deactivateDomain manageDomainAdminLimits manageDomainServices manageCatchAll manageGroupware manageLdapSync manageDomainAliases manageDomainStorage manageAccountServices manageAutomaticMigration manageFoldersQuotas managePasswordPolicy manageWebmailLimits manageFilteredEmail manageSendReceiveRestrictions manageRPOPRestrictions manageTemporaryAddresses manageAccountRecovery managePersonalOrganizer manageSharing manageOutlookConnector manageActiveSync manageIA manageAccounts createAccounts removeAccounts manageAccountsNaming changeAccountsPassword changeAccountsClass manageAccountsContactInformation manageAccountsWebmailOptions manageGroups createGroups removeGroups manageGroupsNaming manageGroupsMembers manageMaillists createMailLists removeMailLists manageMailListsNaming changeMailListsPassword manageMailListsMembers manageMailListsSubscription manageMailListsPosting manageMailListsMessageHeaders manageMailListsTemplates manageMailListsWebmailOptions manageMailListsServices manageMailListsFoldersQuotas manageMailListsWebmailLimits manageMailListsSendReceiveRestrictions manageAccountClasses createAccountClasses removeAccountClasses renameAccountClasses manageFolderRecipients managePublicFolder createPublicFolder removePublicFolder renamePublicFolder managePublicFoldersQuotas

- `LIST SecurityMethods` — list the admin user's security methods

- `REVOKE securityMethod <methodId>` — revokes the given admin user's security method

- `REVOKE all securityMethods` — revokes all the admin user's security methods



## domain




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `LIST Aliases` — lists aliases for current domain

- `LIST Accounts [wildcard (ex: account*)]` — lists accounts for current domain

- `LIST Groups [wildcard (ex: account*)]` — lists groups for current domain

- `LIST FolderRcpts [wildcard (ex: account*)]` — lists folder recipients for current domain

- `LIST Lists [wildcard (ex: account*)]` — lists mail lists for current domain

- `LIST AccountClasses [wildcard (ex: account*)]` — lists account classes for current domain

- `LIST Ghosts [wildcard (ex: account*)]` — lists ghost accounts waiting for ldap synchronization

- `LIST DomainObjectsInfo [wildcard (ex: account*)]` — lists domain objects with detailed information for current domain

- `LIST SearchFolders [details]` — lists search folders for current domain

- `SHOW RegistryInformation` — shows registry information

- `SHOW StorageInformation [details]` — shows storage files information (with details per file if option present)

- `SHOW StorageStatistics [details|summary][average][raw][mboxDetails][mboxReset]` — shows total or average storage statistics (with details per file if option present)

- `SHOW AccountingStatistics [since <date>][until <date>]` — shows accounting statistics for the last month or a specified period

- `SHOW DisposableMetadataInformation` — shows information about the size occupied by obsolete disposable meta-data in the storage

- `SHOW BrandingElement <faviconPhoto|faviconNPhoto|ajaxPublicPhoto|ajaxPrivatePhoto|standardPublicPhoto|standardPrivatePhoto|mobilePublicPhoto|mobilePrivatePhoto|*>` — shows the binary value of a branding element (base64 encoded)

- `SHOW SearchIndexInformation [diag] [details]` — shows general information about the mail search-index data of the current domain

- `SHOW SearchIndexInformation [diag] allfolders` — shows search-index information for all mail folders containing indexes of the current domain

- `SHOW CalendarSearchIndexInformation [diag] [details]` — shows general information about the calendar search-index data of the current domain

- `SHOW CalendarSearchIndexInformation [diag] allfolders` — shows search-index information for all calendar folders containing indexes of the current domain

- `SHOW ContactSearchIndexInformation [diag] [details]` — shows general information about the contact search-index data of the current domain

- `SHOW ContactSearchIndexInformation [diag] allfolders` — shows search-index information for all contact folders containing indexes of the current domain

- `SHOW SortIndexInformation [details]` — shows general information about the sort-index data of the current domain

- `SHOW SortIndexInformation allfolders` — shows sort-index information for all folders containing sort indexes of the current domain

- `SHOW ConversationIndexInformation [diag] [details]` — shows general information about the conversation-index data of the current domain

- `SHOW postmasterAccount` — shows information about the account with postmaster role

- `PURGE disposableMetadata` — purge obsolete disposable meta-data from the domain

- `PURGE public|account folders <folderName> [, <folderName>]* [<purgeCondition>]` — purge mails from specified folders of all users from the domain

- `RESET ldapSynchronization` — resets the ldap synchronization (any synchronization in progress must be stopped first)

- `RESET postmasterAccount` — resets postmaster account role to the default 'postmaster' account

- `RESET maintenanceDate` — request domain maintenance task to be performed as soon as possible

- `SET [name <name>]` — sets the domain's name - only usable in an UPDATE operation

- `SET [assignedIp <ip>]` — sets the assigned ip

- `SET [services (list of services)]` — sets the services for this domain

- `SET [showWebmailLogin <yes|no>]` — enables/disables displaying this domain at Webmail login

- `SET [createUsersFromLdap <yes|no>]` — enables/disables auto-creation of users authenticated from LDAP

- `SET [publishRcptContacts <yes|no>]` — switch indicating if domain recipients contacts are published

- `SET [enableAppender <yes|no>]` — enables/disables the message appender

- `SET [catchAllType <type>]` — sets the type of Catch-All behaviour

- `SET [catchAllAccountName <value>]` — sets the name of the account used to store all messages with unknown recipient

- `SET [catchAllFolderName <value>]` — sets the name of the folder used to store all messages with unknown recipient

- `SET [enableLDAPSync <yes|no>]` — enables/disables LDAP-AXIGEN synchronization

- `SET [ldapSyncConnectorName <name>]` — sets the name of the LDAP connector to use

- `SET [customerReference <string>]` — sets the customer reference for use with external billing like systems

- `SET [defaultTimezone <timezone>]` — sets the default timezone

- `SET [defaultLanguage <lang>]` — sets the default language

- `SET [disposableMetadataQuotaThreshold <no.>]` — sets the obsolete disposable meta-data quota threshold

- `SET [brandingName <name>]` — sets the branding name

- `SET [enableGravatar <yes|no>]` — enables/disables gravatar

- `SET [enablePushNotificationGenerator <yes|no>]` — enables/disables push notification generator

- `SET [postmasterAccount <name>]` — sets postmaster account role to a specific account (it takes effect immediately, not at commit)

- `ESET appenderHtml` — this text will be appended to all messages sent from this domain

- `ESET BrandingElement <faviconPhoto|faviconNPhoto|ajaxPublicPhoto|ajaxPrivatePhoto|standardPublicPhoto|standardPrivatePhoto|mobilePublicPhoto|mobilePrivatePhoto|*>` — sets the binary value of a branding element (the value must be base64 encoded)

- `CONFIG MIGRATIONDATA` — enters the migrationdata context

- `CONFIG FILTERS` — enters the domain filters context

- `CONFIG adminLimits` — enters the admin limits context

- `CONFIG accountDefaultFilters` — enters the account default filters context

- `CONFIG accountDefaultLimits` — enters the account default limits context

- `CONFIG folderRcptDefaultLimits` — enters the folder recipient default limits context

- `CONFIG autodiscovery` — enters the autodiscovery domain parameters configuration context

- `CONFIG accountDefaultQuotas` — enters the account default quotas context

- `CONFIG accountDefaultSendRecvRestrictions` — enters the account default send/recv restrictions context

- `CONFIG accountDefaultWebmailAdvertising` — enters the account default webmail advertising context

- `CONFIG PUBLIC-FOLDER` — enters the Public Folders context

- `CONFIG PERMISSIONS` — enters the Permissions context

- `CONFIG initialAccountSettings` — enters the initial account settings context

- `ADD Account [name] <name> password <password>` — adds an account to the domain

- `UPDATE Account [name] <name>` — updates an account from the domain

- `REMOVE Account [name] <name>` — removes an account from the domain

- `SHOW Account [name] <name> [ATTR <param>]` — shows the given account

- `ADD Group [name] <name>` — adds a group to the domain

- `UPDATE Group [name] <name>` — updates a group from the domain

- `REMOVE Group [name] <name>` — removes a group from the domain

- `SHOW Group [name] <name> [ATTR <param>]` — shows the given group

- `ADD FolderRcpt [name] <name>` — adds a folder recipient to the domain

- `UPDATE FolderRcpt [name] <name>` — updates a folder recipient from the domain

- `REMOVE FolderRcpt [name] <name>` — removes a folder recipient from the domain

- `SHOW FolderRcpt [name] <name> [ATTR <param>]` — shows the given folder recipient

- `ADD List [name] <listName> password <password> adminEmail <email>` — adds a list to this domain

- `UPDATE List [name] <listName>` — updates a list from this domain

- `REMOVE List [name] <listName>` — removes a list from this domain

- `SHOW List [name] <listName> [ATTR <param>]` — shows the given list

- `ADD Alias <aliasName>` — adds an alias for the domain

- `REMOVE Alias <aliasName>` — removes an alias from the domain

- `ADD accountClass [name] <accountClassName>` — adds an account class for the domain (changes context

- `UPDATE accountClass [name] <accountClassName>` — updates an account class from the domain

- `REMOVE accountClass [name] <accountClassName>` — removes an account class from the domain

- `REMOVE GHOSTS [wildcard (ex: g*)]` — remove ghost accounts from the domain

- `MIGRATE ` — migrate command which has the following parameters: account <accountName> - the local account to which the content will be migrated remoteHost <host> - the address of the remote IMAP server from which the data will be migrated remotePort <port> - the IMAP port of the remote server from which the data will be migrated remoteUser <imap-user> - the email address for the remote account who's data will be migrated remotePass <imap-pass> - the password of the remote account who's data will be migrated [ignoreFolders (folders)] - list of folders separated by spaces not to be migrated (you must escape SPACE in a folder name with "\" even in quotes) [overrideQuota <yes|no>] - specifies if the mailbox quota should be overridden (default: no) [deleteOriginal <yes|no>] - enables/disables deletion of all migrated messages on the remote server (default: no) [structureOnly <yes|no>] - enables migration of only the directory structure (default: no) [verbose <yes|no>] - specifies if the command should be verbose (default: no)

- `MIGRATE LIST` — list running migration jobs for the current domain

- `MIGRATE ATTACH <accountName>` — permanently attach to another CLI session where migration is running for the specified account

- `MIGRATE PEEK <accountName> [<timeout>]` — temporary attach to another CLI session where migration is running for the specified account (default timeout: 10 seconds)

- `MIGRATE ABORT [<accountName>]` — abort one or all migration jobs for the current domain

- `WARNING ` — 

- `LIST Storages` — lists all domain's storages registered to AXIGEN

- `LIST activeStorageTransactions [details]` — List active transactions on domain's storage units registered to AXIGEN; without 'details' argument only the total active transactions list is reported

- `READLOCK Storages` — acquire read lock on all domain's storages registered to AXIGEN

- `READUNLOCK Storages` — release read lock on all domain's storages registered to AXIGEN

- `COMPACT All [forced] [splitAfter <max_size> into <split_storage_usid>]` — compacts all storages registered to AXIGEN

- `COMPACT Storage usid <storage_usid> [forced] [splitAfter <max_size> into <split_storage_usid>]` — compacts a storage from the list

- `COMPACT attach | peek [timeout]` — permanently or temporarily attach to another CLI session where compact is running for the domain

- `COMPACT abort` — abort a running compact job for the domain started from another CLI session

- `SCAN ALL [purge|softPurge][verbose][readOnly][imapLeaks][cachedOnly][clearCache][analyzeStructure][recoverTo <accountName>]` — scan all message storages in order to report storage usage and purge storage leaks

- `SCAN Storage usid <storage_usid> [usid <storage_usid>...] [purge|softPurge][verbose][readOnly][imapLeaks][cachedOnly][clearCache][analyzeStructure][recoverTo <accountName>]` — scan the specified message storages in order to report storage usage and purge storage leaks

- `SCAN DomainContainer` — scan the internal domain container in order to report storage usage

- `SCAN PublicFolders` — scan the domain public folders in order to report storage usage

- `SCAN Account <accountName>` — scan the account folders in order to report storage usage

- `SCAN attach | peek [timeout]` — permanently or temporarily attach to another CLI session where scan is running for the domain

- `SCAN abort` — abort a running scan job for the domain started from another CLI session

- `ENABLE [detailed] StorageStatistics` — enables I/O statistics for all storages in domain

- `ENABLE traceLog DomainContainer [folder <foldername>]` — enable trace log for internal domain container folders

- `ENABLE traceLog PublicFolders [folder <foldername>]` — enable trace log for domain public folders

- `ENABLE traceLog Account <accountName> [allfolders | folder <foldername>]` — enable trace log for account folders

- `ENABLE traceLog NODB` — enable trace log for named objects database

- `DISABLE StorageStatistics` — disables I/O statistics for all storages in domain

- `DISABLE traceLog DomainContainer [folder <foldername>]` — disable trace log for internal domain container folders

- `DISABLE traceLog PublicFolders [folder <foldername>]` — disable trace log for domain public folders

- `DISABLE traceLog Account <accountName> [allfolders | folder <foldername>]` — disable trace log for account folders

- `DISABLE traceLog NODB` — disable trace log for named objects database

- `UPGRADE Storage` — upgrade storage representation of configuration data and folders to current version

- `REPAIR Accounts [skip-stage-3] <accountName> [<accountName>...]` — try to recover lost accounts. Use [skip-stage-3] to avoid scanning message storages in search for lost mails

- `REPAIR attach | peek [timeout]` — permanently or temporarily attach to another CLI session where repair accounts is running for the domain

- `REPAIR abort` — abort a running repair accounts job for the domain started from another CLI session

- `SYNCCONTACTS ` — synchronize Domain Contacts folder with domain's objects contact information

- `FINDINVALIDMSG <accountName> [<accountName>...] [purge] [details]` — list and optionally remove faulty messages from specified accounts

- `FINDINVALIDMSG attach | peek [timeout]` — permanently or temporarily attach to another CLI session where find invalid messages is running for the domain

- `FINDINVALIDMSG abort` — abort a running find invalid messages job for the domain started from another CLI session

- `RECOVER domain <domainName> [clearpassword|setpassword <newPasswd>|defaultpassword <defaultPasswd>] [dryrun]` — attempt to recover accounts and messages from the specified domain and migrate them to the current domain

- `RECOVER accounts [setpassword <passwd>] [dryrun]` — attempt to recover accounts and messages from the orphan mailbox containers of the current domain

- `RECOVER attach | peek [timeout]` — permanently or temporarily attach to another CLI session where recover domain or accounts is running with this domain as destination

- `RECOVER abort` — abort a running recover domain or accounts job with this domain as destination started from another CLI session

- `PURGEMAPIPROPS [onMessages] [onFolders] [specialFolders] [onContacts] [dryrun] [regex] [<accountNamePattern/folderPathPattern>...]` — remove the MAPI properties associated with the specified folders and/or their messages from the given accounts

- `PURGEMAPIPROPS attach | peek [timeout]` — permanently or temporarily attach to another CLI session where purge mapi properties is running for the domain

- `PURGEMAPIPROPS abort` — abort a running purge mapi properties job for the domain started from another CLI session

- `REMOVE TmpSearchFolders <all | account [wildcard (ex: account*)]>` — remove the temporary search folders for selected users



## domain-create




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW ` — shows information about this context

- `SET [name <name>]` — sets the domain's name

- `SET [postmasterPassword <pass>]` — sets the password to the postmaster account

- `SET [domainLocation <unitLocationURI>]` — syntax: unitLocationURI = [file://]path[?maxFiles=<fileCount>&maxFileSize=<fileSize>]

- `SET [wmFilterTemplatePath <sieve file path>]` — sets the path to the wmfilter template sieve file for this domain

- `SET [domainObjectsLocation <unitLocationURI>]` — syntax: unitLocationURI = [file://]path[?maxFiles=<fileCount>&maxFileSize=<fileSize>]

- `SET [groupwareSupport <yes|no>]` — enables/disables MACL support for this domain

- `ADD MessagesLocation <unitLocationURI>` — syntax: unitLocationURI = [file://]path[?maxFiles=<fileCount>&maxFileSize=<fileSize>]

- `REMOVE MessagesLocation <path>` — removes a messages storage location



## domain-edit




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW ` — shows information about this context

- `SET [domainLocation <unitLocationURI>]` — syntax: unitLocationURI = [file://]path[?maxFiles=<fileCount>&maxFileSize=<fileSize>&readOnly=<yes|no>]

- `SET [wmFilterTemplatePath <sieve file path>]` — sets the path to the wmfilter template sieve file for this domain

- `SET [domainObjectsLocation <unitLocationURI>]` — syntax: unitLocationURI = [file://]path[?maxFiles=<fileCount>&maxFileSize=<fileSize>&readOnly=<yes|no>]

- `SET [groupwareSupport <yes|no>]` — enables/disables MACL support for this domain

- `ADD MessagesLocation <unitLocationURI>` — syntax: unitLocationURI = [file://]path[?maxFiles=<fileCount>&maxFileSize=<fileSize>&readOnly=<yes|no>]

- `UPDATE MessagesLocation <path> <newUnitLocationURI>` — updates a messages storage location

- `REMOVE MessagesLocation <path>` — removes a messages storage location

- `COMPACT all|domainStorage|domainObjectsStorage|messagesStorage [forced]` — Compact all or some of domain storage units; the domain must not be enabled

- `REPAIR domainContainer [forced|reset]` — Repair the internal domain container; the domain must not be enabled

- `REPAIR publicContainer [forced|reset|resetFlags]` — Repair the public domain container; the domain must not be enabled

- `REPAIR attach | peek [timeout]` — permanently or temporarily attach to another CLI session where repair domain internal or public container is running

- `REPAIR abort` — abort a running repair domain internal or public container job started from another CLI session



## domain/FILTERS




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `LIST ScriptFilters` — lists the script filters defined

- `LIST ActiveFilters` — lists the active filters

- `LIST Filters` — lists both categories of filters

- `LIST Presets [wildcard (ex: off*)]` — lists filter presets for current domain

- `ADD ScriptFilter [name] <name> file <file>` — adds a script filter

- `UPDATE ScriptFilter [name] <name>` — updates a script filter

- `REMOVE ScriptFilter [name] <name>` — removes a script filter from the list

- `SHOW ScriptFilter [name] <name> [ATTR <param>]` — shows the given script filter

- `ADD ActiveFilter [priority] <no.> filterName <name> filterType <type>` — adds an active filter to the active filter list

- `UPDATE ActiveFilter [priority] <no.>` — updates a filter

- `REMOVE ActiveFilter [priority] <no.>` — removes a filter from the active filter list

- `SHOW ActiveFilter [priority] <no.> [ATTR <param>]` — shows the given filter

- `ADD Preset [name] <name>` — adds a filter preset to the domain

- `UPDATE Preset [name] <name>` — updates a filter preset from the domain

- `REMOVE Preset [name] <name>` — removes a filter preset from the domain

- `REMOVE Presets` — removes all filter presets from the domain

- `SHOW Preset [name] <name> [ATTR <param>]` — shows the given filter presets

- `UPDATE WAFilter [<path>]` — update webadmin filters with the contents of the specified by path or uploaded via CLI connection

- `SHOW WAFilter [<path>]` — download to the file specified by path or via CLI connection the webadmin filters

- `LIST Whitelist` — list address patterns from Whitelist (available only for the accounts context)

- `ADD Whitelist <address_pattern>` — add an address pattern to Whitelist (available only for the accounts context)

- `REMOVE Whitelist <address_pattern>` — remove an address pattern from Whitelist (available only for the accounts context)

- `RESET Whitelist` — remove all address patterns from Whitelist (available only for the accounts context)

- `LIST Blacklist` — list address patterns from Blacklist (available only for the accounts context)

- `ADD Blacklist <address_pattern>` — add an address pattern to Blacklist (available only for the accounts context)

- `REMOVE Blacklist <address_pattern>` — remove an address pattern from Blacklist (available only for the accounts context)

- `RESET Blacklist` — remove all address patterns from Blacklist (available only for the accounts context)

- `UPDATE WMFilterTemplate [<path>]` — update webmail template filters with the contents of the specified by path or uploaded via CLI connection

- `SHOW WMFilterTemplate [<path>]` — download to the file specified by path or via CLI connection the webmail template filters

- `SET propagateFilterTemplate` — sets the propagateFilterTemplate property for this domain (1, true, yes or opposites

- `SHOW propagateFilterTemplate` — gets (and shows) the propagateFilterTemplate property for this domain



## domain/FILTERS/Preset




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [name <name>]` — sets the filter preset's name - only usable in an UPDATE operation

- `LIST Filters` — lists all filter configurations

- `ADD Filter [name] <name>` — adds a filter config to the filter preset

- `UPDATE Filter [name] <name>` — updates a filter config from the filter preset

- `REMOVE Filter [name] <name>` — removes a filter config from the filter preset

- `SHOW Filter [name] <name> [ATTR <param>]` — shows the given filter config



## domain/FILTERS/Preset/Filter




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [name <name>]` — sets the filter config's name - only usable in an UPDATE operation

- `SET [enabled <enabled>]` — sets the filter config's enabled - only usable in an UPDATE operation



## domain/FILTERS/ScriptFilter




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [name <name>]` — sets the name of the filter - only usable in an UPDATE operation

- `SET [type <type>]` — sets the type of the script filter

- `SET [file <path>]` — sets the path to the file where the script is located (must be a relative path)

- `UPLOAD filter` — uploads a sieve filter to the location pointed by the "file" parameter



## domain/MIGRATIONDATA




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [enable <yes|no>]` — enables migration of accounts for this domain

- `SET [createPremiumAccounts <yes|no>]` — when enabled, automigration creates premium accounts according to license restrictions

- `SET [enableContinuousMigration <yes|no>]` — when enabled, automigration is performed at every user login

- `SET [remoteImapHost <host>]` — sets the name of remote IMAP machine from which the domain's accounts are migrated

- `SET [remoteImapPort <port>]` — sets the IMAP server's port on the remote machine

- `SET [remoteSmtpHost <host>]` — sets the name of remote SMTP machine from which the domain's accounts are migrated

- `SET [remoteSmtpPort <port>]` — sets the SMTP server's port on the remote machine

- `SET [defaultAccountClassName <class>]` — sets the default account class name

- `SET [enableMigrationCommand <yes|no>]` — when enabled, the command specified as migration command is executed after the account is created

- `SET [migrationCommand <command>]` — sets the migration external command, including arguments

- `SET [enableDebugLogging <yes|no>]` — when enabled, debug information is logged



## domain/PERMISSIONS




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — switches back to the previous context

- `DONE ` — switches back to the previous context

- `LIST Permissions` — lists all available permissions

- `GRANT permission (<permNames>) admin-user [name] <name>` — grants permissions to user

- `REVOKE permission (<permNames>) admin-user [name] <name>` — revokes permissions to user

- `DENY permission (<permNames>) admin-user [name] <name>` — denies permissions to user

- `GRANT permission (<permNames>) admin-group [name] <name>` — grants permissions to group

- `REVOKE permission (<permNames>) admin-group [name] <name>` — revokes permissions to group

- `DENY permission (<permNames>) admin-group [name] <name>` — denies permissions to group permissions:  - manageSubdomains manageDomainConfig manageDomainFilters backupDomain restoreDomain deactivateDomain manageDomainAdminLimits manageDomainServices manageCatchAll manageGroupware manageLdapSync manageDomainAliases manageDomainStorage manageAccountServices manageAutomaticMigration manageFoldersQuotas managePasswordPolicy manageWebmailLimits manageFilteredEmail manageSendReceiveRestrictions manageRPOPRestrictions manageTemporaryAddresses manageAccountRecovery managePersonalOrganizer manageSharing manageOutlookConnector manageActiveSync manageIA manageAccounts createAccounts removeAccounts manageAccountsNaming changeAccountsPassword changeAccountsClass manageAccountsContactInformation manageAccountsWebmailOptions manageGroups createGroups removeGroups manageGroupsNaming manageGroupsMembers manageMaillists createMailLists removeMailLists manageMailListsNaming changeMailListsPassword manageMailListsMembers manageMailListsSubscription manageMailListsPosting manageMailListsMessageHeaders manageMailListsTemplates manageMailListsWebmailOptions manageMailListsServices manageMailListsFoldersQuotas manageMailListsWebmailLimits manageMailListsSendReceiveRestrictions manageAccountClasses createAccountClasses removeAccountClasses renameAccountClasses manageFolderRecipients managePublicFolder createPublicFolder removePublicFolder renamePublicFolder managePublicFoldersQuotas



## domain/PUBLIC-FOLDER




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `LIST MBoxes [details]` — list the available mboxes

- `SET [name <name>]` — sets the name of the Public Folders

- `CONFIG QUOTAS` — enters the quotas context

- `ADD Mbox <name> [type mail|events|tasks|journal|notes|contacts]` — adds a mbox to the Public Folders

- `REMOVE Mbox <name>` — removes a mbox from the Public Folders

- `SHOW SearchIndexInformation [diag]` — shows general information about the mail search-index data of the public folders of the current domain

- `SHOW SearchIndexInformation [diag] allfolders` — shows search-index information for all public mail folders containing indexes of the current domain

- `SHOW SearchIndexInformation [diag] folder <foldername>` — shows search-index information for the provided public mail folder of the current domain

- `SHOW CalendarSearchIndexInformation [diag]` — shows general information about the calendar search-index data of the public folders of the current domain

- `SHOW CalendarSearchIndexInformation [diag] allfolders` — shows search-index information for all public calendar folders containing indexes of the current domain

- `SHOW CalendarSearchIndexInformation [diag] folder <foldername>` — shows search-index information for the provided public calendar folder of the current domain

- `SHOW ContactSearchIndexInformation [diag]` — shows general information about the contact search-index data of the public folders of the current domain

- `SHOW ContactSearchIndexInformation [diag] allfolders` — shows search-index information for all public contact folders containing indexes of the current domain

- `SHOW ContactSearchIndexInformation [diag] folder <foldername>` — shows search-index information for the provided public contact folder of the current domain

- `SHOW SortIndexInformation` — shows general information about the sort-index data of the public folders of the current domain

- `SHOW SortIndexInformation allfolders` — shows sort-index information for all public folders containing sort indexes of the current domain

- `SHOW SortIndexInformation folder <foldername>` — shows sort-index information for the provided public folder of the current domain

- `PURGE calendarMetadata` — purge calendar metadata for the public folders of the current domain

- `PURGE calendarMetadata folder <folderName>` — purge calendar metadata for the provided public folder of the current domain



## domain/PUBLIC-FOLDER/QUOTAS




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [mboxCount <count>]` — sets the maximum number of folders

- `SET [totalMessageCount <count>]` — sets maximum number of messages in all folders

- `SET [totalMessageSize <size>]` — sets maximum size in KB of all messages in all folders

- `SET [messageCount <count>]` — sets default maximum number of messages in a folder

- `SET [messageSize <size>]` — sets default maximum size in KB of messages in a folder

- `LIST Mboxes` — list the available mboxes for this account

- `SET MboxQuota mboxName <name> messageCount <count> messageSize <size>` — sets quotas for a given mbox

- `SHOW MboxQuota mboxName <name>` — shows quotas for a given mbox



## domain/account




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `LIST Aliases` — lists aliases for current account

- `LIST Delegates` — list delegate permissions for current account

- `LIST MEMBERSHIP [noGroups][noLists][sameDomain][directReference]` — list groups and/or mailing lists referring to the current account

- `LIST Folders` — lists folders for current account

- `SET [name <name>]` — sets the account's name - only usable in an UPDATE operation

- `SET [password <password> [respectEnforcement <yes|no>] ]` — sets password for the account, optionally respecting current enforcement rules

- `SET [mustChangePass <yes|no>]` — forces the user to change password at the next login

- `SET [accountType <basic|premium>]` — sets the account type

- `SET [twoFactorConfigured <yes|no>]` — sets if two factor authentication has been configured

- `SET [customerReference <string>]` — sets the customer reference for use with external billing like systems

- `SET [publishContactInfo <yes|no>]` — enables/disables this recipient published in domain contacts

- `SET [filteringOption <pass|discard|sendNDR|moveToFilteredEmail|moveToFilteredEmailWithIC>]` — 

- `ADD securityMethod <sms|email> <target>` — adds the corresponding security method

- `LIST SecurityMethods` — list account security methods

- `REVOKE securityMethod <methodId>` — revokes the given account security method

- `REVOKE all securityMethods` — revokes all account security methods

- `CONFIG WebmailData` — enters the webmaildata context

- `CONFIG Filters` — enters the filters context

- `CONFIG Quotas` — enters the quota context

- `CONFIG Limits` — enters the limits context

- `CONFIG SendRecvRestrictions` — enters the send/recv restrictions context

- `CONFIG ContactInfo` — enters the contact information context

- `CONFIG WebmailAdvertising` — enters the webmail advertising context

- `ADD Alias <aliasName>` — adds an alias for the account

- `REMOVE Alias <aliasName>` — removes an alias from the account

- `ADD Delegate <delegateName> resource <calendar|tasks|freebusy> permissions r|w|rw` — adds a delegate permission for a resource

- `REMOVE Delegate <delegateName> [resource <calendar|tasks|freebusy>]` — remove a delegate permission for a resource or on all resources

- `PURGE account folders <folderName> [, <folderName>]* [<purgeCondition>]` — purge mails from specified folders of the current user

- `PURGE calendarMetadata` — purge calendar metadata belonging to the current user

- `PURGE calendarMetadata folder <folderName>` — purge calendar metadata from the specified folder belonging to the current user

- `PURGE caldav propertiesForFolder <folderName>` — purge caldav properties (such as calendar color, order) for the specified local calendar folder

- `PURGE caldav sharedProperties` — purge caldav shared properties (such as calendar color, order) for all the shared calendar folders accessible to the user

- `PURGE caldav inviteMessages` — purge caldav invite messages (purges all the invite notifications received by this user)

- `RESET ldapAssociation` — resets the ldap associations

- `RESET messageMetadata attachments|calendar [allfolders|folder <foldername> [<folderName>]* ]` — resets part of cached message metadata to force reevaluation of some properties

- `RESET folder <folderName> [<folderName>]*` — re-creates the folder attempting to keep the messages; in case of a search folder a new search is initiated

- `RESET messageConversationIds` — forces synchronization of conversation IDs between conversation database and messages database

- `SHOW RegistryInformation` — shows registry information

- `SHOW SearchIndexInformation [diag]` — shows general information about the mail search-index data of the current account

- `SHOW SearchIndexInformation [diag] allfolders` — shows search-index information for all mail folders containing indexes of the current account

- `SHOW SearchIndexInformation [diag] folder <foldername>` — shows search-index information for the provided mail folder of the current account

- `SHOW CalendarSearchIndexInformation [diag]` — shows general information about the calendar search-index data of the current account

- `SHOW CalendarSearchIndexInformation [diag] allfolders` — shows search-index information for all calendar folders containing indexes of the current account

- `SHOW CalendarSearchIndexInformation [diag] folder <foldername>` — shows search-index information for the provided calendar folder of the current account

- `SHOW ContactSearchIndexInformation [diag]` — shows general information about the contact search-index data of the current account

- `SHOW ContactSearchIndexInformation [diag] allfolders` — shows search-index information for all contact folders containing indexes of the current account

- `SHOW ContactSearchIndexInformation [diag] folder <foldername>` — shows search-index information for the provided contact folder of the current account

- `SHOW SortIndexInformation` — shows general information about the sort-index data of the current account

- `SHOW SortIndexInformation allfolders` — shows sort-index information for all folders containing sort indexes of the current account

- `SHOW SortIndexInformation folder <foldername>` — shows sort-index information for the provided folder of the current account

- `SHOW ConversationIndexInformation [diag]` — shows general information about the conversation-index data of the current account

- `ARCHIVE folder <folderName> older than <days>` — archive items older than specified number of days from given folder

- `INHERIT SETTINGS FROM domainDefaults` — inherit settings from domain defaults (explicit values will not be reset)

- `INHERIT SETTINGS FROM accountClass <accountClassName>` — inherit settings from specified account class (explicit values will not be reset)

- `IMPORTCONTACTS file <file_path> [folder <name>] [duplicatesPolicy <allow|ignore|mergeServerWins|mergeClientWins>]` — import contacts from a CSV file, defaults: folder 'Contacts', duplicatesPolicy allow

- `REPAIR contacts in folder <folder> remove invalid bday` — removes non-ISO8601 bday fields from specified contacts folder

- `REPAIR contacts in folder <folder> remove duplicates` — removes duplicates from specified contacts folder based on first name, last name, email uniqueness



## domain/account/ContactInfo




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [firstName <string>]` — sets the first name for this user

- `SET [lastName <string>]` — sets the last name for this user

- `SET [nickName <string>]` — sets the nick name for this user

- `SET [personalEmail <string>]` — sets the personal email for this user

- `SET [businessEmail <string>]` — sets the business email for this user

- `SET [phone <string>]` — sets the phone for this user

- `SET [mobilePhone <string>]` — sets the mobile phone for this user

- `SET [homePhone <string>]` — sets the home phone for this user

- `SET [businessPhone <string>]` — sets the business phone for this user

- `SET [homeAddress <string>]` — sets the home address for this user

- `SET [businessAddress <string>]` — sets the business address for this user

- `SET [personalVoIPAddress <string>]` — sets the personalVoIPAddress for this user

- `SET [birthday <string>]` — sets the birthday for this user

- `SET [spouseName <string>]` — sets the spouseName for this user

- `SET [businessVoIPAddress <string>]` — sets the businessVoIPAddress for this user

- `SET [company <string>]` — sets the company for this user

- `SET [department <string>]` — sets the department for this user

- `SET [office <string>]` — sets the office for this user

- `SET [position <string>]` — sets the position for this user

- `SET [profession <string>]` — sets the profession for this user

- `SET [managerName <string>]` — sets the managerName for this user

- `SET [assistantName <string>]` — sets the assistantName for this user

- `SET [website <string>]` — sets the website for this user

- `SET [yahooMessengerId <string>]` — sets the yahooMessengerId for this user

- `SET [googleTalkId <string>]` — sets the googleTalkId for this user

- `SET [liveMessengerAddress <string>]` — sets the liveMessengerAddress for this user

- `SET [icqNumber <string>]` — sets the icqNumber for this user

- `SET [aolScreenName <string>]` — sets the aolScreenName for this user

- `SET [skypeId <string>]` — sets the skypeId for this user

- `SET [title <string>]` — sets the title for this user

- `SET [middleName <string>]` — sets the middleName for this user

- `SET [suffix <string>]` — sets the suffix for this user

- `SET [businessFax <string>]` — sets the businessFax for this user

- `ESET contactNotes` — sets the contact notes



## domain/account/FILTERS




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `LIST ScriptFilters` — lists the script filters defined

- `LIST ActiveFilters` — lists the active filters

- `LIST Filters` — lists both categories of filters

- `ADD ScriptFilter [name] <name> file <file>` — adds a script filter

- `UPDATE ScriptFilter [name] <name>` — updates a script filter

- `REMOVE ScriptFilter [name] <name>` — removes a script filter from the list

- `SHOW ScriptFilter [name] <name> [ATTR <param>]` — shows the given script filter

- `ADD ActiveFilter [priority] <no.> filterName <name> filterType <type>` — adds an active filter to the active filter list

- `UPDATE ActiveFilter [priority] <no.>` — updates a filter

- `REMOVE ActiveFilter [priority] <no.>` — removes a filter from the active filter list

- `SHOW ActiveFilter [priority] <no.> [ATTR <param>]` — shows the given filter

- `UPDATE WAFilter [<path>]` — update webadmin filters with the contents of the specified by path or uploaded via CLI connection

- `SHOW WAFilter [<path>]` — download to the file specified by path or via CLI connection the webadmin filters

- `UPDATE WMFilter [<path>]` — update webmail filters with the contents of the specified by path or uploaded via CLI connection (available only for the accounts context)

- `SHOW WMFilter [<path>]` — download to the file specified by path or via CLI connection the webmail filters (available only for the accounts context)

- `LIST Whitelist` — list address patterns from Whitelist (available only for the accounts context)

- `ADD Whitelist <address_pattern>` — add an address pattern to Whitelist (available only for the accounts context)

- `REMOVE Whitelist <address_pattern>` — remove an address pattern from Whitelist (available only for the accounts context)

- `RESET Whitelist` — remove all address patterns from Whitelist (available only for the accounts context)

- `LIST Blacklist` — list address patterns from Blacklist (available only for the accounts context)

- `ADD Blacklist <address_pattern>` — add an address pattern to Blacklist (available only for the accounts context)

- `REMOVE Blacklist <address_pattern>` — remove an address pattern from Blacklist (available only for the accounts context)

- `RESET Blacklist` — remove all address patterns from Blacklist (available only for the accounts context)

- `RESET ` — Inherit filters



## domain/account/Filters




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `LIST ScriptFilters` — lists the script filters defined

- `LIST ActiveFilters` — lists the active filters

- `LIST Filters` — lists both categories of filters

- `ADD ScriptFilter [name] <name> file <file>` — adds a script filter

- `UPDATE ScriptFilter [name] <name>` — updates a script filter

- `REMOVE ScriptFilter [name] <name>` — removes a script filter from the list

- `SHOW ScriptFilter [name] <name> [ATTR <param>]` — shows the given script filter

- `ADD ActiveFilter [priority] <no.> filterName <name> filterType <type>` — adds an active filter to the active filter list

- `UPDATE ActiveFilter [priority] <no.>` — updates a filter

- `REMOVE ActiveFilter [priority] <no.>` — removes a filter from the active filter list

- `SHOW ActiveFilter [priority] <no.> [ATTR <param>]` — shows the given filter

- `UPDATE WAFilter [<path>]` — update webadmin filters with the contents of the specified by path or uploaded via CLI connection

- `SHOW WAFilter [<path>]` — download to the file specified by path or via CLI connection the webadmin filters

- `UPDATE WMFilter [<path>]` — update webmail filters with the contents of the specified by path or uploaded via CLI connection (available only for the accounts context)

- `SHOW WMFilter [<path>]` — download to the file specified by path or via CLI connection the webmail filters (available only for the accounts context)

- `LIST Whitelist` — list address patterns from Whitelist (available only for the accounts context)

- `ADD Whitelist <address_pattern>` — add an address pattern to Whitelist (available only for the accounts context)

- `REMOVE Whitelist <address_pattern>` — remove an address pattern from Whitelist (available only for the accounts context)

- `RESET Whitelist` — remove all address patterns from Whitelist (available only for the accounts context)

- `LIST Blacklist` — list address patterns from Blacklist (available only for the accounts context)

- `ADD Blacklist <address_pattern>` — add an address pattern to Blacklist (available only for the accounts context)

- `REMOVE Blacklist <address_pattern>` — remove an address pattern from Blacklist (available only for the accounts context)

- `RESET Blacklist` — remove all address patterns from Blacklist (available only for the accounts context)

- `RESET ` — Inherit filters



## domain/account/Limits




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [sentMessagesCount <count>]` — max. no. of mails a user can send in a specified interval

- `SET [sentRecipientsCount <count>]` — max. no. of recipients to which a user can send in a specified interval

- `SET [sentMessagesSize <size>]` — max. size of mails a user can send in a specified interval

- `SET [sentMessagesInterval <interval>]` — specified interval in seconds

- `SET [webmailAttSize <size>]` — size limit of an attachment that can be uploaded using Webmail

- `SET [webmailAttCount <count>]` — attachments number limit for a mail composed in Webmail

- `SET [webmailMessageSize <size>]` — size limit for a mail (body + attachments) composed in Webmail

- `SET [temporaryAliasesCount <no>]` — sets the temporary email address count limit

- `SET [temporaryAliasesInterval <no>]` — sets the temporary email address duration limit

- `SET [htmlFilterLevel <number>]` — sets the security level for a html mail body (0-3)

- `SET [archivingPolicy ([folderPerYear] [folderPerMonth])` — configure the behaviour of the archiving feature

- `SET [sentOverquotaFileName <path>]` — name of the file containing template email message sent as notification in case of sent overquota

- `SET [sentOverquotaEmailAddress <email>]` — email address where overquota notification email is sent (empty string means disabled)

- `LIST sentRecipientsExceptions` — list patterns for recipient emails ignored from sent quota policy rules

- `ADD sentRecipientsExceptions <pattern>` — add an email pattern for recipients ignored from sent quota policy rules

- `REMOVE sentRecipientsExceptions <pattern>` — remove an email pattern for recipients ignored from sent quota policy rules

- `SET [services (list of services)]` — sets the services

- `SET [pop3ConnectionCount <count>]` — no. of simultaneous POP3 connections

- `SET [imapConnectionCount <count>]` — no. of simultaneous IMAP connections

- `SET [webmailRCPTCount <count>]` — max. no. of recipients for an email composed using Webmail

- `SET [webmailSessionCount <count>]` — maximum simultaneous webmail sessions

- `SET [rpopConnectionCount <count>]` — sets the maximum number of RPOP user is allowed to define

- `SET [rpopRetrievalInterval <no>]` — sets the minimum time interval in minutes between two RPOP retrievals on the same connection

- `SET [enableActiveSync <yes|no>]` — enables/disables activeSync

- `SET [activeSyncOptions (options)]` — sets activeSync options. Values: email|contact|pim

- `SET [enableOutlookConnector <yes|no>]` — enables/disables outlookConnector

- `SET [enableConversationIndex <yes|no>]` — enables/disables conversations index

- `SET [enableWebPersonalOrganizer <yes|no>]` — enables/disables PersonalOrganizer

- `SET [enableSharing <yes|no>]` — enables/disables sharing

- `SET [welcomeMessageEnabled <yes|no>]` — enables/disables the post of a welcome message in an account's mailbox

- `SET [welcomeMessageFileName <path>]` — sets name of file containing template email message sent as welcome message

- `SET [allowIdentityConfirmation <yes|no>]` — enables/disables the use of Identity Confirmation

- `SET [editableContactInfo <yes|no>]` — enables/disables contact info being editable

- `SET [enableAutoMigration <yes|no>]` — enables/disables the account's auto migration

- `SET [enableCalAvailabilitySharing <yes|no>]` — enables/disables calendar availability sharing for users in this domain

- `SET [localizedImapFolderNames <yes|no>]` — enable/disable localization of folder names accessed using IMAP service

- `SET [enableZoom <yes|no>]` — allow the usage of Zoom related features

- `SET [enableTeams <yes|no>]` — allow the usage of Teams related features

- `SET [passwordEnforcementEnabled <yes|no>]` — enables/disables the password enforcement policy

- `SET [minimumPasswordLength <size>]` — sets minimum size of the password

- `SET [maximumPasswordLength <size>]` — sets maximum size of the password

- `SET [requiredPasswordCharacters <characters>]` — sets required characters that must be present in the password

- `SET [passExpirationEnabled <yes|no>]` — enables/disables password expiration

- `SET [passExpirationInterval <days>]` — sets the interval of time in days that may pass from the moment the password was changed until the moment it expires and can not be used

- `SET [passExpirationType <interval|date]` — set password expiration policy to either interval or date based

- `SET [passExpirationDate <"20 Jun 2018" | "Wed, 20 Jun 2018 02:15:34 +0300">]` — set password expiration date

- `SET [passRenewalInterval <days>]` — sets the interval of time that must pass from the moment of the last change of the password until a new change can be performed

- `SET [passExpirationWarningEnabled <yes|no>]` — enables/disables sending of a warning message in case of password expiration

- `SET [passExpirationWarningInterval <days>]` — sets the interval of time in days after which warning message is send

- `SET [passExpirationWarningFileName <path>]` — sets name of file containing template email message sent as password expiration warning

- `SET [passExpirationWarningSentDaily <yes|no>]` — enables/disables the password expiration warning to be sent every day during the expiration warning interval

- `SET [passHistorySize <count>]` — sets the number of consecutive changed passwords that can not be used as new password when a change of password is performed

- `SET [passUnchangeable <yes|no>]` — enables/disables the capability for an user to change his/her password

- `SET [passwordRecoveryMethods ([secretQuestion] [email] [sms])]` — sets the methods available for password recovery

- `SET [usernameRecoveryMethods ([email])]` — sets the methods available for user name recovery

- `SET [passwordRecoveryEmailFileName <path>]` — name of the file containing the email message template sent to the user's alternative email address for password recovery

- `SET [passwordRecoverySmsFileName <path>]` — name of the file containing the SMS message template sent to the user's phone number for password recovery

- `SET [usernameRecoveryEmailFileName <path>]` — name of the file containing the email message template sent to the user's alternative email address for username recovery

- `SET [usernameRecoverySmsFileName <path>]` — name of the file containing the SMS message template sent to the user's phone number for username recovery

- `SET [accountSecurityAlternativeEmailAddressEnabled <yes|no>]` — enables/disables the use of an alternative email address for account security

- `SET [accountSecurityPhoneNumberEnabled <yes|no>]` — enables/disables the use of a phone number for account security

- `SET [accountSecuritySmsConnector <smsConnectorName>]` — configures the SMS Connector to be used for sending SMS to the configured phone number

- `SET [accountSecurityMandatory <yes|no>]` — enforces the end-user configuration of the account security methods

- `SET [accountSecurityUpdateInterval <days>]` — sets the time interval (in days) after which the account security update dialog is displayed to the end-user

- `SET [twoFactorAuthEnabled <disabled|enabled|mandatory>]` — enables/disables two factor authentication

- `SET [twoFactorAuthCommunicationMethods ([email] [sms] [authApp])]` — sets the communication methods available for two factor authentication

- `SET [twoFactorAuthEmailFileName <path>]` — name of the file containing the email message template sent to the user's alternative email address for two factor authentication

- `SET [twoFactorAuthSmsFileName <path>]` — name of the file containing the SMS message template sent to the user's phone number for two factor authentication

- `RESET <attr>` — Set an attribute to be inherited

- `RESET sentRecipientsExceptions` — Inherit email patterns for recipients ignored from sent quota policy rules

- `SHOW sendQuota` — Show current send quota status

- `RESET sendQuota` — Reset send quota status



## domain/account/Quotas




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [mboxCount <count>]` — sets the maximum number of folders

- `SET [totalMessageCount <count>]` — sets maximum number of messages in all folders

- `SET [totalMessageSize <size>]` — sets maximum size in KB of all messages in all folders

- `SET [messageCount <count>]` — sets default maximum number of messages in a folder

- `SET [messageSize <size>]` — sets default maximum size in KB of messages in a folder

- `SET [quotaLimitThreshold <size>]` — sets percent of quota which triggers an alert

- `SET [quotaLimitNotificationInterval <size>]` — sets the minimum interval(in minutes) between two quota limit notifications

- `SET [quotaLimitNotificationFileName <path>]` — sets name of file containing template of quota limit notification message

- `SET [quotaLimitNotificationEnabled <yes|no>]` — enables/disables the quota limit email notification

- `SET [quotaLimitPushNotificationEnabled <yes|no>]` — enables/disables the quota limit push notification

- `SET [quotaSendMessageThreshold <percent>]` — sets percent of quota which blocks user from message sending

- `SET [filteredEmailSizeQuota <size>]` — sets maximum size in KB of all messages in "Filtered email"

- `SET [filteredEmailCountQuota <count>]` — sets maximum number of messages in "filtered email" folder

- `SET [autopurgeAgeLimit <days>]` — sets the minimum age in days of purged emails

- `SET [autopurgeFolders <names>]` — sets the list of names automatically purged folders

- `LIST Mboxes` — list the available mboxes for this account

- `SET MboxQuota mboxName <name> messageCount <count> messageSize <size>` — sets quotas for a given mbox

- `SHOW MboxQuota mboxName <name>` — shows quotas for a given mbox

- `RESET <attr>` — Set an attribute to be inherited



## domain/account/SendRecvRestrictions




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [enableSendRestrictions <yes|no>]` — enables/disables the send restrictions

- `SET [sendPolicy <choice>]` — values: denyAnyDomain|allowAnyDomain|allowLocalDomain|allowLocalDomainAndSubdomains

- `SET [enableRecvRestrictions <yes|no>]` — enables/disables the recv restrictions

- `SET [recvPolicy <choice>]` — values: denyAnyDomain|allowAnyDomain|allowLocalDomain|allowLocalDomainAndSubdomains

- `LIST sendPolicyExceptions` — list send policy exceptions

- `LIST recvPolicyExceptions` — list recv policy exceptions

- `ADD sendPolicyException <string>` — add send policy exceptions

- `ADD recvPolicyException <string>` — add recv policy exceptions

- `REMOVE sendPolicyException <string>` — remove send policy exceptions

- `REMOVE recvPolicyException <string>` — remove recv policy exceptions

- `RESET <attr>` — set an attribute to be inherited

- `RESET sendPolicyExceptions` — set send policy exceptions to be inherited

- `RESET recvPolicyExceptions` — set recv policy exceptions to be inherited



## domain/account/WebmailAdvertising




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [enableTopBanner <yes|no>]` — enables/disables top webmail banner

- `SET [enableRightBanner <yes|no>]` — enables/disables right webmail banner

- `SET [enableBottomBanner <yes|no>]` — enables/disables bottom webmail banner

- `ESET topBannerContent` — sets the content of the top banner

- `ESET rightBannerContent` — sets the content of the right banner

- `ESET bottomBannerContent` — sets the content of the bottom banner

- `RESET <attr>` — Set an attribute to be inherited



## domain/account/WebmailData




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [skin <skin>]` — sets the skin for webmail

- `SET [pageSize <pageSize>]` — sets page size

- `SET [saveToSent <yes|no>]` — sets keep a mail copy in "Sent" folder

- `SET [deleteToTrash <yes|no>]` — sets delete mail to trash

- `SET [hideDeletedMessages <yes|no>]` — sets hide messages marked for deletion via imap from webmail

- `SET [autoRefreshInterval <minutes>]` — sets Webmail automatic refresh interval stated in minutes

- `SET [confirmMailDelete <yes|no>]` — sets confirmation of mail delete

- `SET [confirmFolderEmpty <yes|no>]` — sets confirmation of empty folder

- `SET [htmlFilterLevel <no.>]` — sets the security level for a html mail body

- `SET [language <language>]` — sets the webmail's language

- `SET [usePublicContacts <yes|no>]` — indicator if the account should use the domain public contacts in addressbook context

- `SET [useRcptContacts <yes|no>]` — Indicator if the account should use the domain recipient contacts in addressbook context

- `SET [requestReadReceipts <yes|no>]` — enable/disable requesting of read receipts

- `SET [sendReadReceipts <always|never|ask>]` — enable/disable sending of read receipts

- `SET [requestDeliveryReceipts <yes|no>]` — enable/disable requesting of delivery receipts

- `SET [autoAddRecipients <yes|no>]` — sets flag for automatically adding recipients from sent mails to the Collected Addresses folder

- `SET [enableConversationView <yes|no>]` — enable/disable conversation view

- `SET [timezone <string>]` — sets the timezone preference

- `SET [weekStartDay <sunday|monday|tuesday|wednesday|thursday|friday|saturday>]` — sets the week start day

- `SET [purgeTrashMessageSelector <all|"">]` — sets the message selector used to purge trash folder

- `SET [purgeSpamMessageSelector <all|"">]` — sets the message selector used to purge spam folder

- `SET [workingDays <(sunday monday tuesday wednesday thursday friday saturday)>]` — sets working days mask

- `SET [startWorkingTime  <hh:mm[:ss]>]` — sets daily start working time

- `SET [endWorkingTime <hh:mm[:ss]>]` — sets daily end working time

- `SET [dateFormat <new format>]` — sets format for displaying dates

- `SET [timeFormat <new format>]` — sets format for displaying times

- `SET [secretQuestion <newSecretQuestion> <newSecretAnswer>]` — sets the secret question and answer used for password recovery

- `SET [calendarType <gregorian|persian>]` — sets the calendar system to use

- `LIST signatures` — lists the account's signatures

- `SHOW signature [id <signatureId>]|[name <signatureName>]` — dumps one of the account's signatures

- `ESET signature [id <signatureId>]|[name <signatureName>]` — sets one of the account's signatures

- `ADD signature name <signatureName> [type <signatureType>]` — adds a new entry to the account's signatures

- `REMOVE signature [id <signatureId>]|[name <signatureName>]` — removes one of the account's signatures

- `SHOW uiSettings` — dumps the account's UI settings

- `ESET uiSettings` — sets the account's UI settings | ! | requires the Webmail service to be stopped

- `RESET uiSettings` — reset unconfigurable UI settings to default

- `SHOW uiCustomSettings` — dumps the account's custom UI settings

- `ESET uiCustomSettings` — sets the account's custom UI settings | ! | requires the Webmail service to be stopped

- `RESET uiCustomSettings` — reset unconfigurable UI custom settings to default



## domain/accountClass




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `CONFIG Filters` — enters the filters context

- `CONFIG Quotas` — enters the quota context

- `CONFIG Limits` — enters the limits context

- `CONFIG SendRecvRestrictions` — enters the send/recv restrictions context

- `CONFIG WebmailAdvertising` — enters the webmail advertising context

- `SET [name <name>]` — sets the account class name - only usable in an UPDATE operation



## domain/accountClass/Filters




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `LIST ScriptFilters` — lists the script filters defined

- `LIST ActiveFilters` — lists the active filters

- `LIST Filters` — lists both categories of filters

- `ADD ScriptFilter [name] <name> file <file>` — adds a script filter

- `UPDATE ScriptFilter [name] <name>` — updates a script filter

- `REMOVE ScriptFilter [name] <name>` — removes a script filter from the list

- `SHOW ScriptFilter [name] <name> [ATTR <param>]` — shows the given script filter

- `ADD ActiveFilter [priority] <no.> filterName <name> filterType <type>` — adds an active filter to the active filter list

- `UPDATE ActiveFilter [priority] <no.>` — updates a filter

- `REMOVE ActiveFilter [priority] <no.>` — removes a filter from the active filter list

- `SHOW ActiveFilter [priority] <no.> [ATTR <param>]` — shows the given filter

- `RESET ` — Inherit filters



## domain/accountClass/Limits




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [sentMessagesCount <count>]` — max. no. of mails a user can send in a specified interval

- `SET [sentRecipientsCount <count>]` — max. no. of recipients to which a user can send in a specified interval

- `SET [sentMessagesSize <size>]` — max. size of mails a user can send in a specified interval

- `SET [sentMessagesInterval <interval>]` — specified interval in seconds

- `SET [webmailAttSize <size>]` — size limit of an attachment that can be uploaded using Webmail

- `SET [webmailAttCount <count>]` — attachments number limit for a mail composed in Webmail

- `SET [webmailMessageSize <size>]` — size limit for a mail (body + attachments) composed in Webmail

- `SET [temporaryAliasesCount <no>]` — sets the temporary email address count limit

- `SET [temporaryAliasesInterval <no>]` — sets the temporary email address duration limit

- `SET [htmlFilterLevel <number>]` — sets the security level for a html mail body (0-3)

- `SET [archivingPolicy ([folderPerYear] [folderPerMonth])` — configure the behaviour of the archiving feature

- `SET [sentOverquotaFileName <path>]` — name of the file containing template email message sent as notification in case of sent overquota

- `SET [sentOverquotaEmailAddress <email>]` — email address where overquota notification email is sent (empty string means disabled)

- `LIST sentRecipientsExceptions` — list patterns for recipient emails ignored from sent quota policy rules

- `ADD sentRecipientsExceptions <pattern>` — add an email pattern for recipients ignored from sent quota policy rules

- `REMOVE sentRecipientsExceptions <pattern>` — remove an email pattern for recipients ignored from sent quota policy rules

- `SET [services (list of services)]` — sets the services

- `SET [pop3ConnectionCount <count>]` — no. of simultaneous POP3 connections

- `SET [imapConnectionCount <count>]` — no. of simultaneous IMAP connections

- `SET [webmailRCPTCount <count>]` — max. no. of recipients for an email composed using Webmail

- `SET [webmailSessionCount <count>]` — maximum simultaneous webmail sessions

- `SET [rpopConnectionCount <count>]` — sets the maximum number of RPOP user is allowed to define

- `SET [rpopRetrievalInterval <no>]` — sets the minimum time interval in minutes between two RPOP retrievals on the same connection

- `SET [enableActiveSync <yes|no>]` — enables/disables activeSync

- `SET [activeSyncOptions (options)]` — sets activeSync options. Values: email|contact|pim

- `SET [enableOutlookConnector <yes|no>]` — enables/disables outlookConnector

- `SET [enableConversationIndex <yes|no>]` — enables/disables conversations index

- `SET [enableWebPersonalOrganizer <yes|no>]` — enables/disables PersonalOrganizer

- `SET [enableSharing <yes|no>]` — enables/disables sharing

- `SET [welcomeMessageEnabled <yes|no>]` — enables/disables the post of a welcome message in an account's mailbox

- `SET [welcomeMessageFileName <path>]` — sets name of file containing template email message sent as welcome message

- `SET [allowIdentityConfirmation <yes|no>]` — enables/disables the use of Identity Confirmation

- `SET [editableContactInfo <yes|no>]` — enables/disables contact info being editable

- `SET [enableAutoMigration <yes|no>]` — enables/disables the account's auto migration

- `SET [enableCalAvailabilitySharing <yes|no>]` — enables/disables calendar availability sharing for users in this domain

- `SET [localizedImapFolderNames <yes|no>]` — enable/disable localization of folder names accessed using IMAP service

- `SET [enableZoom <yes|no>]` — allow the usage of Zoom related features

- `SET [enableTeams <yes|no>]` — allow the usage of Teams related features

- `SET [passwordEnforcementEnabled <yes|no>]` — enables/disables the password enforcement policy

- `SET [minimumPasswordLength <size>]` — sets minimum size of the password

- `SET [maximumPasswordLength <size>]` — sets maximum size of the password

- `SET [requiredPasswordCharacters <characters>]` — sets required characters that must be present in the password

- `SET [passExpirationEnabled <yes|no>]` — enables/disables password expiration

- `SET [passExpirationInterval <days>]` — sets the interval of time in days that may pass from the moment the password was changed until the moment it expires and can not be used

- `SET [passExpirationType <interval|date]` — set password expiration policy to either interval or date based

- `SET [passExpirationDate <"20 Jun 2018" | "Wed, 20 Jun 2018 02:15:34 +0300">]` — set password expiration date

- `SET [passRenewalInterval <days>]` — sets the interval of time that must pass from the moment of the last change of the password until a new change can be performed

- `SET [passExpirationWarningEnabled <yes|no>]` — enables/disables sending of a warning message in case of password expiration

- `SET [passExpirationWarningInterval <days>]` — sets the interval of time in days after which warning message is send

- `SET [passExpirationWarningFileName <path>]` — sets name of file containing template email message sent as password expiration warning

- `SET [passExpirationWarningSentDaily <yes|no>]` — enables/disables the password expiration warning to be sent every day during the expiration warning interval

- `SET [passHistorySize <count>]` — sets the number of consecutive changed passwords that can not be used as new password when a change of password is performed

- `SET [passUnchangeable <yes|no>]` — enables/disables the capability for an user to change his/her password

- `SET [passwordRecoveryMethods ([secretQuestion] [email] [sms])]` — sets the methods available for password recovery

- `SET [usernameRecoveryMethods ([email])]` — sets the methods available for user name recovery

- `SET [passwordRecoveryEmailFileName <path>]` — name of the file containing the email message template sent to the user's alternative email address for password recovery

- `SET [passwordRecoverySmsFileName <path>]` — name of the file containing the SMS message template sent to the user's phone number for password recovery

- `SET [usernameRecoveryEmailFileName <path>]` — name of the file containing the email message template sent to the user's alternative email address for username recovery

- `SET [usernameRecoverySmsFileName <path>]` — name of the file containing the SMS message template sent to the user's phone number for username recovery

- `SET [accountSecurityAlternativeEmailAddressEnabled <yes|no>]` — enables/disables the use of an alternative email address for account security

- `SET [accountSecurityPhoneNumberEnabled <yes|no>]` — enables/disables the use of a phone number for account security

- `SET [accountSecuritySmsConnector <smsConnectorName>]` — configures the SMS Connector to be used for sending SMS to the configured phone number

- `SET [accountSecurityMandatory <yes|no>]` — enforces the end-user configuration of the account security methods

- `SET [accountSecurityUpdateInterval <days>]` — sets the time interval (in days) after which the account security update dialog is displayed to the end-user

- `SET [twoFactorAuthEnabled <disabled|enabled|mandatory>]` — enables/disables two factor authentication

- `SET [twoFactorAuthCommunicationMethods ([email] [sms] [authApp])]` — sets the communication methods available for two factor authentication

- `SET [twoFactorAuthEmailFileName <path>]` — name of the file containing the email message template sent to the user's alternative email address for two factor authentication

- `SET [twoFactorAuthSmsFileName <path>]` — name of the file containing the SMS message template sent to the user's phone number for two factor authentication

- `RESET <attr>` — Set an attribute to be inherited

- `RESET sentRecipientsExceptions` — Inherit email patterns for recipients ignored from sent quota policy rules



## domain/accountClass/Quotas




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [mboxCount <count>]` — sets the maximum number of folders

- `SET [totalMessageCount <count>]` — sets maximum number of messages in all folders

- `SET [totalMessageSize <size>]` — sets maximum size in KB of all messages in all folders

- `SET [messageCount <count>]` — sets default maximum number of messages in a folder

- `SET [messageSize <size>]` — sets default maximum size in KB of messages in a folder

- `SET [quotaLimitThreshold <size>]` — sets percent of quota which triggers an alert

- `SET [quotaLimitNotificationInterval <size>]` — sets the minimum interval(in minutes) between two quota limit notifications

- `SET [quotaLimitNotificationFileName <path>]` — sets name of file containing template of quota limit notification message

- `SET [quotaLimitNotificationEnabled <yes|no>]` — enables/disables the quota limit email notification

- `SET [quotaLimitPushNotificationEnabled <yes|no>]` — enables/disables the quota limit push notification

- `SET [quotaSendMessageThreshold <percent>]` — sets percent of quota which blocks user from message sending

- `SET [filteredEmailSizeQuota <size>]` — sets maximum size in KB of all messages in "Filtered email"

- `SET [filteredEmailCountQuota <count>]` — sets maximum number of messages in "filtered email" folder

- `SET [autopurgeAgeLimit <days>]` — sets the minimum age in days of purged emails

- `SET [autopurgeFolders <names>]` — sets the list of names automatically purged folders

- `RESET <attr>` — Set an attribute to be inherited



## domain/accountClass/SendRecvRestrictions




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [enableSendRestrictions <yes|no>]` — enables/disables the send restrictions

- `SET [sendPolicy <choice>]` — values: denyAnyDomain|allowAnyDomain|allowLocalDomain|allowLocalDomainAndSubdomains

- `SET [enableRecvRestrictions <yes|no>]` — enables/disables the recv restrictions

- `SET [recvPolicy <choice>]` — values: denyAnyDomain|allowAnyDomain|allowLocalDomain|allowLocalDomainAndSubdomains

- `LIST sendPolicyExceptions` — list send policy exceptions

- `LIST recvPolicyExceptions` — list recv policy exceptions

- `ADD sendPolicyException <string>` — add send policy exceptions

- `ADD recvPolicyException <string>` — add recv policy exceptions

- `REMOVE sendPolicyException <string>` — remove send policy exceptions

- `REMOVE recvPolicyException <string>` — remove recv policy exceptions

- `RESET <attr>` — set an attribute to be inherited

- `RESET sendPolicyExceptions` — set send policy exceptions to be inherited

- `RESET recvPolicyExceptions` — set recv policy exceptions to be inherited



## domain/accountClass/WebmailAdvertising




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [enableTopBanner <yes|no>]` — enables/disables top webmail banner

- `SET [enableRightBanner <yes|no>]` — enables/disables right webmail banner

- `SET [enableBottomBanner <yes|no>]` — enables/disables bottom webmail banner

- `ESET topBannerContent` — sets the content of the top banner

- `ESET rightBannerContent` — sets the content of the right banner

- `ESET bottomBannerContent` — sets the content of the bottom banner

- `RESET <attr>` — Set an attribute to be inherited



## domain/accountDefaultFilters




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — switches back to the previous context

- `DONE ` — switches back to the previous context

- `LIST ScriptFilters` — lists the script filters defined

- `LIST ActiveFilters` — lists the active filters

- `LIST Filters` — lists both categories of filters

- `LIST Presets [wildcard (ex: off*)]` — lists filter presets for current domain

- `ADD ScriptFilter [name] <name> file <file>` — adds a script filter

- `UPDATE ScriptFilter [name] <name>` — updates a script filter

- `REMOVE ScriptFilter [name] <name>` — removes a script filter from the list

- `SHOW ScriptFilter [name] <name> [ATTR <param>]` — shows the given script filter

- `ADD ActiveFilter [priority] <no.> filterName <name> filterType <type>` — adds an active filter to the active filter list

- `UPDATE ActiveFilter [priority] <no.>` — updates a filter

- `REMOVE ActiveFilter [priority] <no.>` — removes a filter from the active filter list

- `SHOW ActiveFilter [priority] <no.> [ATTR <param>]` — shows the given filter

- `ADD Preset [name] <name>` — adds a filter preset to the domain

- `UPDATE Preset [name] <name>` — updates a filter preset from the domain

- `REMOVE Preset [name] <name>` — removes a filter preset from the domain

- `REMOVE Presets` — removes all filter presets from the domain

- `SHOW Preset [name] <name> [ATTR <param>]` — shows the given filter presets

- `UPDATE WAFilter [<path>]` — update webadmin filters with the contents of the specified by path or uploaded via CLI connection

- `SHOW WAFilter [<path>]` — download to the file specified by path or via CLI connection the webadmin filters

- `LIST Whitelist` — list address patterns from Whitelist (available only for the accounts context)

- `ADD Whitelist <address_pattern>` — add an address pattern to Whitelist (available only for the accounts context)

- `REMOVE Whitelist <address_pattern>` — remove an address pattern from Whitelist (available only for the accounts context)

- `RESET Whitelist` — remove all address patterns from Whitelist (available only for the accounts context)

- `LIST Blacklist` — list address patterns from Blacklist (available only for the accounts context)

- `ADD Blacklist <address_pattern>` — add an address pattern to Blacklist (available only for the accounts context)

- `REMOVE Blacklist <address_pattern>` — remove an address pattern from Blacklist (available only for the accounts context)

- `RESET Blacklist` — remove all address patterns from Blacklist (available only for the accounts context)

- `UPDATE WMFilterTemplate [<path>]` — update webmail template filters with the contents of the specified by path or uploaded via CLI connection

- `SHOW WMFilterTemplate [<path>]` — download to the file specified by path or via CLI connection the webmail template filters

- `SET propagateFilterTemplate` — sets the propagateFilterTemplate property for this domain (1, true, yes or opposites

- `SHOW propagateFilterTemplate` — gets (and shows) the propagateFilterTemplate property for this domain



## domain/accountDefaultFilters/ScriptFilter




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [name <name>]` — sets the name of the filter - only usable in an UPDATE operation

- `SET [type <type>]` — sets the type of the script filter

- `SET [file <path>]` — sets the path to the file where the script is located (must be a relative path)

- `UPLOAD filter` — uploads a sieve filter to the location pointed by the "file" parameter



## domain/accountDefaultLimits




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [sentMessagesCount <count>]` — max. no. of mails a user can send in a specified interval

- `SET [sentRecipientsCount <count>]` — max. no. of recipients to which a user can send in a specified interval

- `SET [sentMessagesSize <size>]` — max. size of mails a user can send in a specified interval

- `SET [sentMessagesInterval <interval>]` — specified interval in seconds

- `SET [webmailAttSize <size>]` — size limit of an attachment that can be uploaded using Webmail

- `SET [webmailAttCount <count>]` — attachments number limit for a mail composed in Webmail

- `SET [webmailMessageSize <size>]` — size limit for a mail (body + attachments) composed in Webmail

- `SET [temporaryAliasesCount <no>]` — sets the temporary email address count limit

- `SET [temporaryAliasesInterval <no>]` — sets the temporary email address duration limit

- `SET [htmlFilterLevel <number>]` — sets the security level for a html mail body (0-3)

- `SET [archivingPolicy ([folderPerYear] [folderPerMonth])` — configure the behaviour of the archiving feature

- `SET [sentOverquotaFileName <path>]` — name of the file containing template email message sent as notification in case of sent overquota

- `SET [sentOverquotaEmailAddress <email>]` — email address where overquota notification email is sent (empty string means disabled)

- `LIST sentRecipientsExceptions` — list patterns for recipient emails ignored from sent quota policy rules

- `ADD sentRecipientsExceptions <pattern>` — add an email pattern for recipients ignored from sent quota policy rules

- `REMOVE sentRecipientsExceptions <pattern>` — remove an email pattern for recipients ignored from sent quota policy rules

- `SET [services (list of services)]` — sets the services

- `SET [pop3ConnectionCount <count>]` — no. of simultaneous POP3 connections

- `SET [imapConnectionCount <count>]` — no. of simultaneous IMAP connections

- `SET [webmailRCPTCount <count>]` — max. no. of recipients for an email composed using Webmail

- `SET [webmailSessionCount <count>]` — maximum simultaneous webmail sessions

- `SET [rpopConnectionCount <count>]` — sets the maximum number of RPOP user is allowed to define

- `SET [rpopRetrievalInterval <no>]` — sets the minimum time interval in minutes between two RPOP retrievals on the same connection

- `SET [enableActiveSync <yes|no>]` — enables/disables activeSync

- `SET [activeSyncOptions (options)]` — sets activeSync options. Values: email|contact|pim

- `SET [enableOutlookConnector <yes|no>]` — enables/disables outlookConnector

- `SET [enableConversationIndex <yes|no>]` — enables/disables conversations index

- `SET [enableWebPersonalOrganizer <yes|no>]` — enables/disables PersonalOrganizer

- `SET [enableSharing <yes|no>]` — enables/disables sharing

- `SET [welcomeMessageEnabled <yes|no>]` — enables/disables the post of a welcome message in an account's mailbox

- `SET [welcomeMessageFileName <path>]` — sets name of file containing template email message sent as welcome message

- `SET [allowIdentityConfirmation <yes|no>]` — enables/disables the use of Identity Confirmation

- `SET [editableContactInfo <yes|no>]` — enables/disables contact info being editable

- `SET [enableAutoMigration <yes|no>]` — enables/disables the account's auto migration

- `SET [enableCalAvailabilitySharing <yes|no>]` — enables/disables calendar availability sharing for users in this domain

- `SET [localizedImapFolderNames <yes|no>]` — enable/disable localization of folder names accessed using IMAP service

- `SET [enableZoom <yes|no>]` — allow the usage of Zoom related features

- `SET [enableTeams <yes|no>]` — allow the usage of Teams related features

- `SET [passwordEnforcementEnabled <yes|no>]` — enables/disables the password enforcement policy

- `SET [minimumPasswordLength <size>]` — sets minimum size of the password

- `SET [maximumPasswordLength <size>]` — sets maximum size of the password

- `SET [requiredPasswordCharacters <characters>]` — sets required characters that must be present in the password

- `SET [passExpirationEnabled <yes|no>]` — enables/disables password expiration

- `SET [passExpirationInterval <days>]` — sets the interval of time in days that may pass from the moment the password was changed until the moment it expires and can not be used

- `SET [passExpirationType <interval|date]` — set password expiration policy to either interval or date based

- `SET [passExpirationDate <"20 Jun 2018" | "Wed, 20 Jun 2018 02:15:34 +0300">]` — set password expiration date

- `SET [passRenewalInterval <days>]` — sets the interval of time that must pass from the moment of the last change of the password until a new change can be performed

- `SET [passExpirationWarningEnabled <yes|no>]` — enables/disables sending of a warning message in case of password expiration

- `SET [passExpirationWarningInterval <days>]` — sets the interval of time in days after which warning message is send

- `SET [passExpirationWarningFileName <path>]` — sets name of file containing template email message sent as password expiration warning

- `SET [passExpirationWarningSentDaily <yes|no>]` — enables/disables the password expiration warning to be sent every day during the expiration warning interval

- `SET [passHistorySize <count>]` — sets the number of consecutive changed passwords that can not be used as new password when a change of password is performed

- `SET [passUnchangeable <yes|no>]` — enables/disables the capability for an user to change his/her password

- `SET [passwordRecoveryMethods ([secretQuestion] [email] [sms])]` — sets the methods available for password recovery

- `SET [usernameRecoveryMethods ([email])]` — sets the methods available for user name recovery

- `SET [passwordRecoveryEmailFileName <path>]` — name of the file containing the email message template sent to the user's alternative email address for password recovery

- `SET [passwordRecoverySmsFileName <path>]` — name of the file containing the SMS message template sent to the user's phone number for password recovery

- `SET [usernameRecoveryEmailFileName <path>]` — name of the file containing the email message template sent to the user's alternative email address for username recovery

- `SET [usernameRecoverySmsFileName <path>]` — name of the file containing the SMS message template sent to the user's phone number for username recovery

- `SET [accountSecurityAlternativeEmailAddressEnabled <yes|no>]` — enables/disables the use of an alternative email address for account security

- `SET [accountSecurityPhoneNumberEnabled <yes|no>]` — enables/disables the use of a phone number for account security

- `SET [accountSecuritySmsConnector <smsConnectorName>]` — configures the SMS Connector to be used for sending SMS to the configured phone number

- `SET [accountSecurityMandatory <yes|no>]` — enforces the end-user configuration of the account security methods

- `SET [accountSecurityUpdateInterval <days>]` — sets the time interval (in days) after which the account security update dialog is displayed to the end-user

- `SET [twoFactorAuthEnabled <disabled|enabled|mandatory>]` — enables/disables two factor authentication

- `SET [twoFactorAuthCommunicationMethods ([email] [sms] [authApp])]` — sets the communication methods available for two factor authentication

- `SET [twoFactorAuthEmailFileName <path>]` — name of the file containing the email message template sent to the user's alternative email address for two factor authentication

- `SET [twoFactorAuthSmsFileName <path>]` — name of the file containing the SMS message template sent to the user's phone number for two factor authentication



## domain/accountDefaultQuotas




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [mboxCount <count>]` — sets the maximum number of folders

- `SET [totalMessageCount <count>]` — sets maximum number of messages in all folders

- `SET [totalMessageSize <size>]` — sets maximum size in KB of all messages in all folders

- `SET [messageCount <count>]` — sets default maximum number of messages in a folder

- `SET [messageSize <size>]` — sets default maximum size in KB of messages in a folder

- `SET [quotaLimitThreshold <size>]` — sets percent of quota which triggers an alert

- `SET [quotaLimitNotificationInterval <size>]` — sets the minimum interval(in minutes) between two quota limit notifications

- `SET [quotaLimitNotificationFileName <path>]` — sets name of file containing template of quota limit notification message

- `SET [quotaLimitNotificationEnabled <yes|no>]` — enables/disables the quota limit email notification

- `SET [quotaLimitPushNotificationEnabled <yes|no>]` — enables/disables the quota limit push notification

- `SET [quotaSendMessageThreshold <percent>]` — sets percent of quota which blocks user from message sending

- `SET [filteredEmailSizeQuota <size>]` — sets maximum size in KB of all messages in "Filtered email"

- `SET [filteredEmailCountQuota <count>]` — sets maximum number of messages in "filtered email" folder

- `SET [autopurgeAgeLimit <days>]` — sets the minimum age in days of purged emails

- `SET [autopurgeFolders <names>]` — sets the list of names automatically purged folders



## domain/accountDefaultSendRecvRestrictions




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [enableSendRestrictions <yes|no>]` — enables/disables the send restrictions

- `SET [sendPolicy <choice>]` — values: denyAnyDomain|allowAnyDomain|allowLocalDomain|allowLocalDomainAndSubdomains

- `SET [enableRecvRestrictions <yes|no>]` — enables/disables the recv restrictions

- `SET [recvPolicy <choice>]` — values: denyAnyDomain|allowAnyDomain|allowLocalDomain|allowLocalDomainAndSubdomains

- `LIST sendPolicyExceptions` — list send policy exceptions

- `LIST recvPolicyExceptions` — list recv policy exceptions

- `ADD sendPolicyException <string>` — add send policy exceptions

- `ADD recvPolicyException <string>` — add recv policy exceptions

- `REMOVE sendPolicyException <string>` — remove send policy exceptions

- `REMOVE recvPolicyException <string>` — remove recv policy exceptions



## domain/accountDefaultWebmailAdvertising




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [enableTopBanner <yes|no>]` — enables/disables top webmail banner

- `SET [enableRightBanner <yes|no>]` — enables/disables right webmail banner

- `SET [enableBottomBanner <yes|no>]` — enables/disables bottom webmail banner

- `ESET topBannerContent` — sets the content of the top banner

- `ESET rightBannerContent` — sets the content of the right banner

- `ESET bottomBannerContent` — sets the content of the bottom banner



## domain/adminLimits




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [maxAccounts <no>]` — (no description)

- `SET [maxMaillists <no>]` — (no description)

- `SET [maxGroups <no>]` — (no description)

- `SET [maxFolderRecipients <no>]` — (no description)

- `SET [maxAccountClasses <no>]` — (no description)

- `SET [maxAccountMessageSizeQuota <no>]` — (no description)

- `SET [maxAccountMessageCountQuota <no>]` — (no description)

- `SET [maxAccountFolderCountQuota <no>]` — (no description)

- `SET [maxAccountFolderMessageSizeQuota <no>]` — (no description)

- `SET [maxAccountFolderMessageCountQuota <no>]` — (no description)

- `SET [maxMaillistMessageSizeQuota <no>]` — (no description)

- `SET [maxMaillistMessageCountQuota <no>]` — (no description)

- `SET [maxMaillistFolderCountQuota <no>]` — (no description)

- `SET [maxMaillistFolderMessageSizeQuota <no>]` — (no description)

- `SET [maxMaillistFolderMessageCountQuota <no>]` — (no description)

- `SET [maxPublicFolderMessageSizeQuota <no>]` — (no description)

- `SET [maxPublicFolderMessageCountQuota <no>]` — (no description)

- `SET [maxPublicFolderFolderCountQuota <no>]` — (no description)

- `SET [maxPublicFolderFolderMessageSizeQuota <no>]` — (no description)

- `SET [maxPublicFolderFolderMessageCountQuota <no>]` — (no description)

- `SET [availableServices (list of domain services)]` — (no description)

- `SET [maxSubdomains <no>]` — (no description)

- `SET [subdomainStorageLocation <path>]` — (no description)

- `SET [subdomainObjectStorageLocation <path>]` — (no description)

- `SET [purgeConstraint <search criteria>]` — (no description)

- `SET [purgeFolders (list of purgeable folders)]` — (no description)

- `SET [maxPremiumMailboxCount <no>]` — (no description)

- `SET [maxSharingMailboxCount <no>]` — (no description)

- `SET [maxPersonalOrganizerMailboxCount <no>]` — (no description)

- `SET [maxOutlookConnectorMailboxCount <no>]` — (no description)

- `SET [maxActiveSyncMailboxCount <no>]` — (no description)

- `SET [maxIAMailboxCount <no>]` — (no description)

- `LIST subdomainMessageStorageLocations` — list message storage locations for this domain

- `LIST reservedRcpts` — list the reserved recipient names for this domain

- `ADD subdomainMessageStorageLocation <path>` — add a message storage location for this domain

- `ADD reservedRcpt <rcpt>` — add a reserved recipient name

- `REMOVE subdomainMessageStorageLocation <path>` — remove a message storage location for this domain

- `REMOVE reservedRcpt <rcpt>` — remove a reserved recipient name



## domain/autodiscovery




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `CONFIG Urls` — enters the autodiscoveryUrls context

- `SHOW Urls` — shows domain autodiscovery URLs

- `ADD HostNameResolver [host] <host> [domain <domain>]` — adds a host name (WebMail URL) to HSP template name mapping

- `UPDATE HostNameResolver [host] <host> [domain <domain>]` — updates a host name (WebMail URL) to HSP template name mapping

- `REMOVE HostNameResolver [host] <host>` — removes a host name (WebMail URL) to HSP template name mapping

- `SHOW HostNameResolver [host] <host>` — shows a virtual host configuration *The domain parameter refers to the HSP template directory

- `LIST HostNameResolvers` — lists the hostname resolvers



## domain/autodiscovery/HostNameResolver




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [host <hostname>]` — set the virtual host name

- `SET [domain <domain>]` — set the HSP template name

- `SET [sslEnable <yes|no>]` — enable/disable SSL on the listener

- `CONFIG SSLCONTROL` — enters the SslControl context



## domain/autodiscovery/HostNameResolver/SSLCONTROL




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [allowedVersions (version list)]` — sets SSL versions allowed

- `SET [maxChainDepth <maxDepth>]` — sets max depth of verification

- `SET [cipherSuite <cipher>]` — sets the cipher suite to be used

- `SET [preferServerCipherSuiteOrder <yes|no>]` — prefer server's ciphers order instead of client's one

- `SET [useEphemeralKey <yes|no>]` — use/not use ephemeral keys

- `SET [certFile <file>]` — sets path for certification chain file

- `SET [caFile <file>]` — sets path for certificate authorities file

- `SET [dhParamFile <file>]` — sets path to Diffie-Hellman param file

- `SET [requestClientAuth <yes|no>]` — request/not request client authentication



## domain/autodiscovery/Urls




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET httpAutodiscoveryUrl <url>` — set the http autodiscovery url

- `SET imapAutodiscoveryUrl <url>` — set the imap autodiscovery url

- `SET pop3AutodiscoveryUrl <url>` — set the pop3 autodiscovery url

- `SET smtpAutodiscoveryUrl <url>` — set the smtp autodiscovery url

- `SET webdavAutodiscoveryUrl <url>` — set the webdav autodiscovery url



## domain/folderRcpt




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `LIST MEMBERSHIP [noGroups][noLists][sameDomain][directReference]` — list groups and/or mailing lists referring to the current folder recipient

- `SHOW RegistryInformation` — shows registry information

- `SET [name <name>]` — sets the folder recipient's name - only usable in an UPDATE operation

- `SET [enable <yes|no>]` — enables/disables the folder recipient

- `SET [mboxName <name>]` — sets the mbox name of this folder recipient)

- `SET [publishContactInfo <yes|no>]` — enables/disables this recipient published in domain contacts

- `SET [domainSendMailAs <yes|no>]` — allow/deny this recipient to be used as sender address by any user of the domain

- `CONFIG FILTERS` — enters the filters context

- `CONFIG LIMITS` — enters the limits context



## domain/folderRcpt/FILTERS




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — switches back to the previous context

- `DONE ` — switches back to the previous context

- `LIST ScriptFilters` — lists the script filters defined

- `LIST ActiveFilters` — lists the active filters

- `LIST Filters` — lists both categories of filters

- `ADD ScriptFilter [name] <name> file <file>` — adds a script filter

- `UPDATE ScriptFilter [name] <name>` — updates a script filter

- `REMOVE ScriptFilter [name] <name>` — removes a script filter from the list

- `SHOW ScriptFilter [name] <name> [ATTR <param>]` — shows the given script filter

- `ADD ActiveFilter [priority] <no.> filterName <name> filterType <type>` — adds an active filter to the active filter list

- `UPDATE ActiveFilter [priority] <no.>` — updates a filter

- `REMOVE ActiveFilter [priority] <no.>` — removes a filter from the active filter list

- `SHOW ActiveFilter [priority] <no.> [ATTR <param>]` — shows the given filter



## domain/folderRcpt/LIMITS




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context



## domain/folderRcptDefaultLimits




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context



## domain/group




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `LIST Addresses` — lists addresses for current group

- `LIST MEMBERSHIP [noGroups][noLists][sameDomain][directReference]` — list groups and/or mailing lists referring to the current group

- `RESET ldapAssociation` — resets the ldap association

- `SHOW RegistryInformation` — shows registry information

- `SET [name <name>]` — sets the group's name - only usable in an UPDATE operation

- `SET [enable <yes|no>]` — enables/disables the group

- `SET [publishContactInfo <yes|no>]` — enables/disables this recipient published in domain contacts

- `SET [membersSendMailAsGroup <yes|no>]` — allow members to use group's email address as sender address

- `SET [distributeEmailTo <members|domain|server|cluster|nobody>]` — Specify group's email distribution target

- `SET [receiveEmailFrom <anybody|server|domain|members|directMembers|nobody>]` — Specify who is allowed to send emails to this group

- `CONFIG FILTERS` — enters the filters context

- `ADD Address <address>` — adds an address for the group

- `REMOVE Address <address>` — removes an address from the group



## domain/group/FILTERS




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — switches back to the previous context

- `DONE ` — switches back to the previous context

- `LIST ScriptFilters` — lists the script filters defined

- `LIST ActiveFilters` — lists the active filters

- `LIST Filters` — lists both categories of filters

- `ADD ScriptFilter [name] <name> file <file>` — adds a script filter

- `UPDATE ScriptFilter [name] <name>` — updates a script filter

- `REMOVE ScriptFilter [name] <name>` — removes a script filter from the list

- `SHOW ScriptFilter [name] <name> [ATTR <param>]` — shows the given script filter

- `ADD ActiveFilter [priority] <no.> filterName <name> filterType <type>` — adds an active filter to the active filter list

- `UPDATE ActiveFilter [priority] <no.>` — updates a filter

- `REMOVE ActiveFilter [priority] <no.>` — removes a filter from the active filter list

- `SHOW ActiveFilter [priority] <no.> [ATTR <param>]` — shows the given filter



## domain/initialAccountSettings




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [weekStartDay <sunday|monday|tuesday|wednesday|thursday|friday|saturday>]` — sets the week start day

- `SET [workingDays <(sunday monday tuesday wednesday thursday friday saturday)>]` — sets working days mask

- `SET [startWorkingTime  <hh:mm[:ss]>]` — sets daily start working time

- `SET [endWorkingTime <hh:mm[:ss]>]` — sets daily end working time

- `SET [dateFormat <new format>]` — sets format for displaying dates

- `SET [timeFormat <new format>]` — sets format for displaying times

- `SET [calendarType <gregorian|persian>]` — sets the calendar type

- `SET [autoAddRecipients <yes|no>]` — sets flag for automatically adding recipients from sent mails to the Collected Addresses folder



## domain/list




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `LIST Users` — lists available users for this list

- `LIST RemoveHeaders` — shows the list of headers that will be removed from a mail

- `LIST MEMBERSHIP [noGroups][noLists][sameDomain][directReference]` — list groups and/or mailling lists referring to the current list

- `SHOW RegistryInformation` — shows registry information

- `SET [name <name>]` — sets the list's name - only usable in an UPDATE operation

- `SET [services (list of services)]` — sets the services enabled for this list

- `SET [password <string>]` — sets the list's mailbox access password

- `SET [subscribeRcpt <rcpt>]` — sets the RCPT used for subscription

- `SET [unsubscribeRcpt <rcpt>]` — sets the RCPT used for unsubscription

- `SET [requestRcpt <rcpt>]` — sets the RCPT used for making a request

- `SET [enabledRcpts (choice set)]` — sets the RCPTs enabled for this list

- `SET [description <description>]` — sets the description of the list

- `SET [adminConfirm <yes|no>]` — sets the adminConfirm parameter

- `SET [senderAllow <choice>]` — sets the senderAllow parameter

- `SET [moderate <choice>]` — sets the moderate parameter

- `SET [ctypeAllow <choice>]` — sets the ctypeAllow parameter

- `SET [adminEmail <email>]` — sets the email for the admin

- `SET [publishContactInfo <yes|no>]` — enables/disables this recipient published in domain contacts

- `SET [rewriteFrom <yes|no>]` — rewrites From, ReplyTo and the envelope to ensure DMARC compliance

- `ESET addHeader` — sets the the headers that will be added to the mail - enters text context

- `ESET bodyBegin` — sets the text that will be inserted before the body - enters text context

- `ESET bodyEnd` — sets the text that will be added to the body to the mail - enters text context

- `ESET unknownCommand` — sets the description of the error in case of a unknown command - enters text context

- `ESET invalidUserName` — sets the description of the error in case of an invalid user name - enters text context

- `ESET notAUser` — sets the description of the error in case the user does not belong to the list - enters text context

- `ESET badConfirmation` — sets the description of the error in case of a bad confirmation - enters text context

- `ESET userAlreadySubscribed` — sets the description of the error in case the user already exists - enters text context

- `ESET invalidFormat` — sets the description of the error in case of an invalid format - enters text context

- `ESET requestNeedsConfirmation` — sets the template that will ask the user for a confirmation - enters text context

- `ESET requestNeedsAdminConfirmation` — sets the template that will tell the user to wait for admins confirmation - enters text context

- `ESET autoRejectResponse` — sets the template that will tell the user that his mail is rejected

- `ESET welcome` — sets the template that will tell the user that he has been created - enters text context

- `ESET goodbye` — sets the template that will tell the user that he has been deleted - enters text context

- `ESET subscribeDenied` — sets the template that will tell the user that he has not been created - enters text context

- `CONFIG WEBMAILDATA` — enters the webmaildata context

- `CONFIG FILTERS` — enters the filters context

- `CONFIG QUOTAS` — enters the quotas context

- `CONFIG LIMITS` — enters the limits context

- `ADD User [email] <email> name <name>` — adds an user to the list

- `UPDATE User [email] <email>` — updates an user from the list

- `REMOVE User [email] <email>` — removes an user from the list

- `SHOW User [email] <email> [ATTR <param>]` — shows an user from the list

- `ADD RemoveHeader <name>` — adds a header to the list of headers to be removed

- `REMOVE RemoveHeader <name>` — removes a header from the list of headers to be removed

- `RESET folder <foldeName> [<folderName>]*` — re-creates the folder attempting to keep the messages; in case of a search folder a new search is initiated



## domain/list/FILTERS




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — switches back to the previous context

- `DONE ` — switches back to the previous context

- `LIST ScriptFilters` — lists the script filters defined

- `LIST ActiveFilters` — lists the active filters

- `LIST Filters` — lists both categories of filters

- `ADD ScriptFilter [name] <name> file <file>` — adds a script filter

- `UPDATE ScriptFilter [name] <name>` — updates a script filter

- `REMOVE ScriptFilter [name] <name>` — removes a script filter from the list

- `SHOW ScriptFilter [name] <name> [ATTR <param>]` — shows the given script filter

- `ADD ActiveFilter [priority] <no.> filterName <name> filterType <type>` — adds an active filter to the active filter list

- `UPDATE ActiveFilter [priority] <no.>` — updates a filter

- `REMOVE ActiveFilter [priority] <no.>` — removes a filter from the active filter list

- `SHOW ActiveFilter [priority] <no.> [ATTR <param>]` — shows the given filter



## domain/list/LIMITS




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [sentMessagesCount <count>]` — max. no. of mails a user can send in a specified interval

- `SET [sentRecipientsCount <count>]` — max. no. of recipients to which a user can send in a specified interval

- `SET [sentMessagesSize <size>]` — max. size of mails a user can send in a specified interval

- `SET [sentMessagesInterval <interval>]` — specified interval in seconds

- `SET [sentOverquotaFileName <path>]` — name of the file containing template email message sent as notification in case of sent overquota

- `SET [sentOverquotaEmailAddress <email>]` — email address where overquota notification email is sent (empty string means disabled)

- `SET [pop3ConnectionCount <count>]` — no. of simultaneous POP3 connections

- `SET [imapConnectionCount <count>]` — no. of simultaneous IMAP connections

- `SET [webmailRCPTCount <count>]` — max. no. of recipients for an email composed using Webmail

- `SET [webmailSessionCount <count>]` — maximum simultaneous webmail sessions

- `SET [webmailAttSize <size>]` — size limit of an attachment that can be uploaded using Webmail

- `SET [webmailAttCount <count>]` — attachments number limit for a mail composed in Webmail

- `SET [webmailMessageSize <size>]` — size limit for a mail (body + attachments) composed in Webmail

- `SET [overQuotaThreshold <percent>]` — sets the percent of used quota which triggers an alert

- `SET [quotaSendMessageThreshold <percent>]` — sets the percent of used quota which blocks user from sending messages

- `SET [archivingPolicy ([folderPerYear] [folderPerMonth])` — configure the behaviour of the archiving feature

- `SET [localizedImapFolderNames <yes|no>]` — enable/disable localization of folder names accessed using IMAP service

- `SET [passExpirationType <interval|date>]` — set password expiration policy to interval or date based

- `SET [passExpirationDate <"Wed, 20 Jun 2018 02:15:34 +0300">]` — set password expiration date

- `LIST sentRecipientsExceptions` — list patterns for recipient emails ignored from sent quota policy rules

- `ADD sentRecipientsExceptions <pattern>` — add an email pattern for recipients ignored from sent quota policy rules

- `REMOVE sentRecipientsExceptions <pattern>` — remove an email pattern for recipients ignored from sent quota policy rules



## domain/list/QUOTAS




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [mboxCount <count>]` — sets the maximum number of folders

- `SET [totalMessageCount <count>]` — sets maximum number of messages in all folders

- `SET [totalMessageSize <size>]` — sets maximum size in KB of all messages in all folders

- `SET [messageCount <count>]` — sets default maximum number of messages in a folder

- `SET [messageSize <size>]` — sets default maximum size in KB of messages in a folder

- `LIST Mboxes` — list the available mboxes for this account

- `SET MboxQuota mboxName <name> messageCount <count> messageSize <size>` — sets quotas for a given mbox

- `SHOW MboxQuota mboxName <name>` — shows quotas for a given mbox



## domain/list/User




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [email <email>]` — sets the user's email - only usable in an UPDATE operation

- `SET [name <name>]` — sets the user's name



## domain/list/WEBMAILDATA




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [skin <skin>]` — sets the skin for webmail

- `SET [pageSize <pageSize>]` — sets page size

- `SET [saveToSent <yes|no>]` — sets keep a mail copy in "Sent" folder

- `SET [deleteToTrash <yes|no>]` — sets delete mail to trash

- `SET [hideDeletedMessages <yes|no>]` — sets hide messages marked for deletion via imap from webmail

- `SET [autoRefreshInterval <minutes>]` — sets Webmail automatic refresh interval stated in minutes

- `SET [confirmMailDelete <yes|no>]` — sets confirmation of mail delete

- `SET [confirmFolderEmpty <yes|no>]` — sets confirmation of empty folder

- `SET [htmlFilterLevel <no.>]` — sets the security level for a html mail body

- `SET [language <language>]` — sets the webmail's language

- `SET [timezone <string>]` — sets the timezone preference

- `LIST signatures` — lists the account's signatures

- `SHOW signature [id <signatureId>]|[name <signatureName>]` — dumps one of the account's signatures

- `ESET signature [id <signatureId>]|[name <signatureName>]` — sets one of the account's signatures

- `ADD signature name <signatureName> [type <signatureType>]` — adds a new entry to the account's signatures

- `REMOVE signature [id <signatureId>]|[name <signatureName>]` — removes one of the account's signatures

- `SHOW uiSettings` — dumps the account's UI settings

- `ESET uiSettings` — sets the account's UI settings | ! | requires the Webmail service to be stopped

- `RESET uiSettings` — reset unconfigurable UI settings to default

- `SHOW uiCustomSettings` — dumps the account's custom UI settings

- `ESET uiCustomSettings` — sets the account's custom UI settings | ! | requires the Webmail service to be stopped

- `RESET uiCustomSettings` — reset unconfigurable UI custom settings to default



## login




- `HELP ` — prints this help message

- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `USER <user>` — CLI username

- `GET VERSION` — gets the AXIGEN version

- `SET CONSOLE-CODES on|off` — sets the color and other console codes on/off

- `SET QUIET off|on` — enables/disables detailed information

- `SHOW ` — shows the options for this context



## server/AUTODISCOVERY/defaultUrls




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET httpAutodiscoveryUrl <url>` — set the http autodiscovery url

- `SET imapAutodiscoveryUrl <url>` — set the imap autodiscovery url

- `SET pop3AutodiscoveryUrl <url>` — set the pop3 autodiscovery url

- `SET smtpAutodiscoveryUrl <url>` — set the smtp autodiscovery url

- `SET webdavAutodiscoveryUrl <url>` — set the webdav autodiscovery url



## server/DNR/nameserver




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [priority <priority>]` — sets the priority of the nameserver

- `SET [address <address>]` — sets the IP of the nameserver

- `SET [timeout <timeout>]` — sets the timeout for first DNS query

- `SET [retries <retries>]` — sets the maximum number of DNS queries retries



## server/FILTERS




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `LIST ScriptFilters` — lists the script filters defined

- `LIST SocketFilters` — lists the socket filters defined

- `LIST IntegratedFilters` — lists the integrated filters defined

- `LIST ActiveFilters` — lists the active filters

- `LIST Filters` — lists all four categories of filters

- `SET [logLevel <level>]` — sets the service's logging level

- `SET [logType <type>]` — sets the service's logging type

- `SET [logHost <host>]` — sets the service's remote logging host

- `ADD ScriptFilter [name] <name> file <file>` — adds a script filter

- `UPDATE ScriptFilter [name] <name>` — updates a script filter

- `REMOVE ScriptFilter [name] <name>` — removes a script filter from the list

- `SHOW ScriptFilter [name] <name> [ATTR <param>]` — shows the given script filter

- `ADD SocketFilter [name] <name> address <addr> protocolFile <file>` — adds a socket filter

- `UPDATE SocketFilter [name] <name>` — updates a socket filter

- `REMOVE SocketFilter [name] <name>` — removes a socket filter from the list

- `SHOW SocketFilter [name] <name> [ATTR <param>]` — shows the given socket filter

- `ADD IntegratedFilter [name] <name> type <type> command <command>` — adds a integrated filter

- `UPDATE IntegratedFilter [name] <name>` — updates a integrated filter

- `REMOVE IntegratedFilter [name] <name>` — removes a integrated filter from the list

- `SHOW IntegratedFilter [name] <name> [ATTR <param>]` — shows the given integrated filter

- `ADD ActiveFilter [priority] <no.> filterName <name> filterType <type>` — adds an active filter to the active filter list

- `UPDATE ActiveFilter [priority] <no.>` — updates a filter

- `REMOVE ActiveFilter [priority] <no.>` — removes a filter from the active filter list

- `SHOW ActiveFilter [priority] <no.> [ATTR <param>]` — shows the given filter

- `LIST Whitelist` — list address patterns from Whitelist (available only for the accounts context)

- `ADD Whitelist <address_pattern>` — add an address pattern to Whitelist (available only for the accounts context)

- `REMOVE Whitelist <address_pattern>` — remove an address pattern from Whitelist (available only for the accounts context)

- `RESET Whitelist` — remove all address patterns from Whitelist (available only for the accounts context)

- `LIST Blacklist` — list address patterns from Blacklist (available only for the accounts context)

- `ADD Blacklist <address_pattern>` — add an address pattern to Blacklist (available only for the accounts context)

- `REMOVE Blacklist <address_pattern>` — remove an address pattern from Blacklist (available only for the accounts context)

- `RESET Blacklist` — remove all address patterns from Blacklist (available only for the accounts context)



## server/FILTERS/SocketFilter




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [name <name>]` — sets the name of the filter - only usable in an UPDATE operation

- `SET [address <addr>]` — sets the address of the filter, used to communicate with the filter

- `SET [protocolFile <path>]` — sets the path to the ASFL file that describes the communication protocol

- `SET [idleTimeout <timeout>]` — sets the inactivity timeout of the connection (in seconds)

- `SET [actionOnMatch <action>]` — sets the action to be taken in case the filter matches an email

- `SET [maxConnections <no.>]` — sets the maximum number of connections that will be made to the filter



## server/IMAP/AccessControl/DenyRule




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `LIST AllowRules` — lists the allow rules for this listener

- `LIST DenyRules` — lists the deny rules for this listener

- `SET [maxConnections <maxConn>]` — sets max number of connections

- `SET [timeInterval <interval>]` — sets the time interval

- `SET [maxIntervalConnections <interval>]` — sets max connections in time interval

- `SET [peerMaxConnections <maxConn>]` — sets sets max connections no. from a single host

- `SET [peerTimeInterval <interval>]` — sets the time interval - single host

- `SET [peerMaxIntervalConnections <interval>]` — sets max connections in time interval - single host

- `ADD DenyRule [ipSet] <ipRange> [enable <yes|no>] [priority <priority>]` — adds a deny rule to the listener

- `UPDATE DenyRule [ipSet] <ipRange> [enable <yes|no>] [priority <priority>]` — updates a deny rule from the listener

- `REMOVE DenyRule [ipSet] <ipRange>` — removes a deny rule from the listener

- `SHOW DenyRule [ipSet] <ipRange>` — shows the given rule

- `ADD AllowRule [ipSet] <ipRange>` — adds an allow rule to the listener

- `UPDATE AllowRule [ipSet] <ipRange>` — updates an allow rule from the listener

- `REMOVE AllowRule [ipSet] <ipRange>` — removes an allow rule from the listener

- `SHOW AllowRule [ipSet] <ipRange>` — shows the given rule



## server/IMAP/listener




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `LIST AllowRules` — lists the allow rules for this listener

- `LIST DenyRules` — lists the deny rules for this listener

- `SET [address <address>]` — sets the listener's address - only usable in an UPDATE operation

- `SET [enable <yes|no>]` — enable/disable the listener

- `SET [maxConnections <maxConn>]` — sets max number of connections

- `SET [timeInterval <interval>]` — sets the time interval

- `SET [maxIntervalConnections <interval>]` — sets max connections in time interval

- `SET [peerMaxConnections <maxConn>]` — sets sets max connections no. from a single host

- `SET [peerTimeInterval <interval>]` — sets the time interval - single host

- `SET [peerMaxIntervalConnections <interval>]` — sets max connections in time interval - single host

- `SET [idleTimeout <timeout>]` — sets the inactivity timeout

- `SET [sslEnable <yes|no>]` — enable/disable SSL on the listener

- `SET [proxyProtocol [disabled|(allowV1|allowV2|allowAll|isOptional)]` — sets options for or disables the proxy protocol

- `SET [proxyProtocolTimeout <timeout>]` — sets the maximum time interval to wait for proxy protocol data

- `SET [nonClusterListener <yes|no>]` — disables/enables listener usage for cluster communication

- `CONFIG SSLCONTROL` — enters the SslControl context

- `ADD DenyRule [ipSet] <ipRange> [enable <yes|no>] [priority <priority>]` — adds a deny rule to the listener

- `UPDATE DenyRule [ipSet] <ipRange> [enable <yes|no>] [priority <priority>]` — updates a deny rule from the listener

- `REMOVE DenyRule [ipSet] <ipRange>` — removes a deny rule from the listener

- `SHOW DenyRule [ipSet] <ipRange>` — shows the given rule

- `ADD AllowRule [ipSet] <ipRange>` — adds an allow rule to the listener

- `UPDATE AllowRule [ipSet] <ipRange>` — updates an allow rule from the listener

- `REMOVE AllowRule [ipSet] <ipRange>` — removes an allow rule from the listener

- `SHOW AllowRule [ipSet] <ipRange>` — shows the given rule



## server/IMAP/listener/SSLCONTROL




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [allowedVersions (version list)]` — sets SSL versions allowed

- `SET [maxChainDepth <maxDepth>]` — sets max depth of verification

- `SET [cipherSuite <cipher>]` — sets the cipher suite to be used

- `SET [preferServerCipherSuiteOrder <yes|no>]` — prefer server's ciphers order instead of client's one

- `SET [useEphemeralKey <yes|no>]` — use/not use ephemeral keys

- `SET [certFile <file>]` — sets path for certification chain file

- `SET [caFile <file>]` — sets path for certificate authorities file

- `SET [dhParamFile <file>]` — sets path to Diffie-Hellman param file

- `SET [requestClientAuth <yes|no>]` — request/not request client authentication



## server/LOG/rule




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [priority <priority>]` — sets the rule's priority - only usable in an UPDATE operation

- `SET [hostname <hostname>]` — sets hostname of the user of this rule

- `SET [module <module>]` — sets module of the user of this rule. valid names: SMTP-IN SMTP-OUT IMAP POP3 WEBMAIL WEBADMIN DNR RPOP CLI PROCESSING LOG

- `REPORTING FTP-BACKUP PROXY_POP3 PROXY_IMAP USERDB PROXY_WEBMAIL FILTERS` — 

- `CALLOG SECURITY JOBLOG SERVER(SRVLOG) MAILBOXAPI` — * = ALL)

- `SET [logLevel <level>]` — sets the log level

- `SET [fileName <name>]` — sets the name of the destination file

- `SET [fileSize <size>]` — sets the maximum size of the destination file in KB

- `SET [fileTime <time>]` — sets the maximum duration the destination file is used in seconds

- `SET [fileCount <count>]` — sets the maximum number of old (saved) files kept

- `SET [rotatePeriod <period>]` — sets the period after which a file change is forced (choice: none|day|week|month)

- `SET [type <type>]` — sets the type of the rule (choice: local|remote)



## server/POP3-Proxy/listener




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `LIST AllowRules` — lists the allow rules for this listener

- `LIST DenyRules` — lists the deny rules for this listener

- `SET [address <address>]` — sets the listener's address - only usable in an UPDATE operation

- `SET [enable <yes|no>]` — enable/disable the listener

- `SET [maxConnections <maxConn>]` — sets max number of connections

- `SET [timeInterval <interval>]` — sets the time interval

- `SET [maxIntervalConnections <interval>]` — sets max connections in time interval

- `SET [peerMaxConnections <maxConn>]` — sets sets max connections no. from a single host

- `SET [peerTimeInterval <interval>]` — sets the time interval - single host

- `SET [peerMaxIntervalConnections <interval>]` — sets max connections in time interval - single host

- `SET [idleTimeout <timeout>]` — sets the inactivity timeout

- `SET [sslEnable <yes|no>]` — enable/disable SSL on the listener

- `SET [proxyProtocol [disabled|(allowV1|allowV2|allowAll|isOptional)]` — sets options for or disables the proxy protocol

- `SET [proxyProtocolTimeout <timeout>]` — sets the maximum time interval to wait for proxy protocol data

- `SET [nonClusterListener <yes|no>]` — disables/enables listener usage for cluster communication

- `SET [listenerDomain <domain>]` — if specified, will act as primary domain for connections made on this listener

- `CONFIG SSLCONTROL` — enters the SslControl context

- `ADD DenyRule [ipSet] <ipRange> [enable <yes|no>] [priority <priority>]` — adds a deny rule to the listener

- `UPDATE DenyRule [ipSet] <ipRange> [enable <yes|no>] [priority <priority>]` — updates a deny rule from the listener

- `REMOVE DenyRule [ipSet] <ipRange>` — removes a deny rule from the listener

- `SHOW DenyRule [ipSet] <ipRange>` — shows the given rule

- `ADD AllowRule [ipSet] <ipRange>` — adds an allow rule to the listener

- `UPDATE AllowRule [ipSet] <ipRange>` — updates an allow rule from the listener

- `REMOVE AllowRule [ipSet] <ipRange>` — removes an allow rule from the listener

- `SHOW AllowRule [ipSet] <ipRange>` — shows the given rule



## server/POP3-Proxy/listener/SSLCONTROL




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [allowedVersions (version list)]` — sets SSL versions allowed

- `SET [maxChainDepth <maxDepth>]` — sets max depth of verification

- `SET [cipherSuite <cipher>]` — sets the cipher suite to be used

- `SET [preferServerCipherSuiteOrder <yes|no>]` — prefer server's ciphers order instead of client's one

- `SET [useEphemeralKey <yes|no>]` — use/not use ephemeral keys

- `SET [certFile <file>]` — sets path for certification chain file

- `SET [caFile <file>]` — sets path for certificate authorities file

- `SET [dhParamFile <file>]` — sets path to Diffie-Hellman param file

- `SET [requestClientAuth <yes|no>]` — request/not request client authentication



## server/REPORT/SNMPTrapDest




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW [ATTR <param>]` — shows information about this context

- `SAVE Config` — saves the server's running configuration

- `LIST Listeners` — lists available listeners

- `LIST SNMPTrapDestinations` — lists available SNMP trap destinations

- `START Service` — starts the report service

- `STOP Service` — stops the report service

- `SET [logLevel <level>]` — sets the service's logging level

- `SET [logType <type>]` — sets the service's logging type

- `SET [logHost <host>]` — sets the service's remote logging host

- `SET [SNMPEnable <yes|no>]` — enables/disables the snmp module

- `SET [SNMPSentTrapsToAllManagers <yes|no>]` — enables/disables sending traps to all managers (including managers not added from configuration)

- `SET [SNMPCommunity <string>]` — sets the SNMP Community string

- `SET [DomainEnable <yes|no>]` — enables/disabled domain level reporting

- `SET [DomainObjectEnable <yes|no>]` — enables/disabled domain object level reporting

- `SET [reportingInterval <weeks>]` — sets the reporting weeks interval

- `ADD Listener [address] <address>` — adds a listener to the service

- `UPDATE Listener [address] <address>` — updates a listener from the service

- `REMOVE Listener [address] <address>` — removes a listener from the service

- `SHOW Listener [address] <address> [ATTR <param>]` — shows the given listener

- `ADD SNMPTrapDestination <address>` — adds a snmp trap destination to the service

- `REMOVE SNMPTrapDestination <address>` — removes a snmp trap destination from the service

- `RESET ` — resets the service to the currently active configuration



## server/SMTP-INCOMING/mappingData




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — switches back to the previous context (does not cancel changes)

- `DONE ` — saves the changes and switches back to previous context

- `SHOW [ATTR <param>]` — shows information about this context

- `SET [userMap <map>]` — a userMap from the list defined on the server

- `SET [mappingHost <host>]` — sets the name or IP address of a default AXIGEN machine to be used if userMap is set to none

- `SET [mappingPort <port>]` — sets the port on which to connect to the default AXIGEN machine



## subdomain-create




- `EXIT/QUIT ` — exits CLI and closes connection to AXIGEN

- `HELP ` — prints this help message

- `BACK ` — cancels any changes made and switches back to the previous context

- `COMMIT ` — commits the changes made in this context

- `SHOW ` — shows information about this context

- `SET [prefix <name>]` — sets the subdomain's prefix

- `SET [postmasterPassword <pass>]` — sets the password to the postmaster account

- `SET [domainLocation <unitLocationURI>]` — syntax: unitLocationURI = [file://]path[?maxFiles=<fileCount>&maxFileSize=<fileSize>]

- `SET [wmFilterTemplatePath <sieve file path>]` — sets the path to the wmfilter template sieve file for this domain

- `SET [domainObjectsLocation <unitLocationURI>]` — syntax: unitLocationURI = [file://]path[?maxFiles=<fileCount>&maxFileSize=<fileSize>]

- `SET [parentDomain <name>]` — sets the parent domain for this subdomain

- `SET [groupwareSupport <yes|no>]` — enables/disables MACL support for this domain

- `ADD MessagesLocation <unitLocationURI>` — syntax: unitLocationURI = [file://]path[?maxFiles=<fileCount>&maxFileSize=<fileSize>]

- `REMOVE MessagesLocation <path>` — removes a messages storage location



