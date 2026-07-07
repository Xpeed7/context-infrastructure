You are a software test engineer familiar with Jira / Zephyr / RTM (Requirement Traceability Matrix) data processing.
Please generate a CSV file that can be imported into Jira based on the files I upload, and strictly follow the rules below.

1. Input Files
I will upload two files:

A Jira Issue exported CSV sample file (used for copying the header structure)
An RTM Excel file (.xlsx), from which the Matrix worksheet must be read


2. Processing Objective
Please read the Matrix worksheet in the RTM Excel file, process and organize the data according to the rules, and generate a new Jira import CSV file.

3. Output Requirements

The output file format must be .csv

The first-row header of the output CSV must be exactly identical to the Jira sample CSV
Field names must match exactly
Column order must match exactly
Renaming is not allowed, and column reordering is not allowed
Please directly generate the new file and return a download link
Do not provide only code or an approach; directly produce the file


4. Source Fields to Read
Read the following fields from the Matrix worksheet of the RTM file:

Business Requirement Epic Name
Business Requirement ID
Business Requirement Name
Functional Requirement ID
Functional Requirement Name
Test Case ID


5. Output Granularity

One row in Matrix = one Jira Issue
However, before output, records must be deduplicated using the following composite key:
Business Requirement ID + Functional Requirement ID


6. Filtering Rules
The following records must be removed and must not enter the final CSV:

Functional Requirement ID = uncovered item

Or Functional Requirement Name = uncovered item

Functional Requirement Name is empty
The generated Summary is empty / blank

Note:

Do not filter out -A- type items (for example, Assumption); keep them and generate Jira Issues as usual


7. Field Mapping Rules
Please populate the fields according to the following rules:

1) Core Fields

Summary = Functional Requirement Name
Issue Type = Story
Project key = OC
Project name = ODP Clearing
Project type = software
Project lead = PaulYau
Priority = Medium
Status = To Do
Votes = 0


2) People Fields

Reporter = FrankYPPei
Creator = FrankYPPei
Watchers = FrankYPPei


3) Custom Fields

Custom field (BR ID) = Business Requirement ID
Custom field (Business Requirement) = Business Requirement Name
Custom field (FR ID) = Functional Requirement ID


4) Epic Link Mapping
Please determine the corresponding Epic Link based on the uploaded RTM file name, using the following rules:

File Name: R1.1-ODP Requirement_Traceabiltiy_Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD01 - Give up and Take Up | Derived Epic Link(s): OC-158
File Name: R1.2-Requirement_Traceabiltiy_Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD02 - Product & Position Netting | Derived Epic Link(s): OC-159
File Name: R1.3.1-Requirement_Traceabiltiy_Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD02 - Position Give Up | Derived Epic Link(s): OC-159
File Name: R1.3-Requirement_Traceabiltiy_Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD02 - Position Transfer | Derived Epic Link(s): OC-159
File Name: R1.4-ODP Requirement_Traceability_Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD01 - Trade Trail | Derived Epic Link(s): OC-158
File Name: R1.5-ODP Requirement_Traceabiltiy_Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD01 - Trade Rectification | Derived Epic Link(s): OC-158
File Name: R1.7-ODP Requirement Traceability Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD01 - Trade Cancellation | Derived Epic Link(s): OC-158
File Name: R1.8-Requirement_Traceabiltiy_Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD01/2/3/4/6/7/10- Post Trade Validation | Derived Epic Link(s): OC-158, OC-159, OC-160, OC-161, OC-163, OC-164, OC-167
File Name: R2.1-ODP Requirement Traceability Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD05 - Covered call request | Derived Epic Link(s): OC-162
File Name: R2.2.1-ODP Requirement_Traceability_Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD07 - General exercise | Derived Epic Link(s): OC-164
File Name: R2.2.2-Requirement_Traceabiltiy_Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD07 - Automatic Exercise Limit | Derived Epic Link(s): OC-164
File Name: R2.2.3-ODP Requirement_Traceabiltiy_Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD06 - Exercise Request | Derived Epic Link(s): OC-163
File Name: R2.2.4-Requirement_Traceabiltiy_Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD09 - Random Assignment Mechanism | Derived Epic Link(s): OC-166
File Name: R2.3-Requirement_Traceabiltiy_Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD04 - Account Management | Derived Epic Link(s): OC-161
File Name: R3-Requirement_Traceabiltiy_Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD01/2/3 - Trade novation and position update | Derived Epic Link(s): OC-158, OC-159, OC-160
File Name: R4.1-Requirement_Traceabiltiy_Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD08 - Exercise and Assignment | Derived Epic Link(s): OC-165
File Name: R4.2-Requirement_Traceabiltiy_Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD12 - Clearing Message | Derived Epic Link(s): OC-169
File Name: R4.3-Requirement_Traceabiltiy_Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD08/34 - FEE, Variation Adjustment & Closing Event | Derived Epic Link(s): OC-165, OC-191
File Name: R4.5.1-Requirement_Traceabiltiy_Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD35 - Accumulated Trade Value Management | Derived Epic Link(s): OC-192
File Name: R4.5-Requirement_Traceabiltiy_Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD08 - Closing Deliveries | Derived Epic Link(s): OC-165
File Name: R5.1-Requirement_Traceabiltiy_Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD03/04/11/19/20/34 - Reference Data Maintenance Management | Derived Epic Link(s): OC-160, OC-161, OC-168, OC-176, OC-177, OC-191
File Name: R5.2-Requirement Traceability Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD03 - Clearing Batches | Derived Epic Link(s): OC-160
File Name: R5.3-Requirement_Traceabiltiy_Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD10 - Clearing Sessions | Derived Epic Link(s): OC-167
File Name: R5.4-Requirement_Traceabiltiy_Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD20 - User and Clearing Account Maintenance | Derived Epic Link(s): OC-177
File Name: R6-Requirement_Traceabiltiy_Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD17-36 - Reporting | Derived Epic Link(s): OC-174, OC-175, OC-176, OC-177, OC-178, OC-179, OC-180, OC-181, OC-182, OC-183, OC-184, OC-185, OC-186, OC-187, OC-188, OC-189, OC-190, OC-191, OC-192, OC-193
File Name: R7.1-Requirement_Traceabiltiy_Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD13 - Capital Adjustment | Derived Epic Link(s): OC-170
File Name: R7.2-Requirement_Traceabiltiy_Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD14 - Final Settlement Price | Derived Epic Link(s): OC-171
File Name: R7.5-Requirement_Traceability_Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD15 - GUI | Derived Epic Link(s): OC-172
File Name: R7.6-Requirement_Traceabiltiy_Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD16 - Non-Functional | Derived Epic Link(s): OC-173
File Name: R7.7-ODP Requirement Traceability Matrix_v1.0.1.xlsx | RTM Function: ODPCL.FD38 - Drop Copy Enhanced | Derived Epic Link(s): OC-195

If one file corresponds to multiple Epic Links, do not guess. First, try to determine the mapping based on Functional Requirement ID / Summary. If the mapping still cannot be uniquely determined, ask me only the minimum necessary clarification question.

8. Description Generation Rule
For all generated rows, write the same fixed text into Description:

No line breaks
Follow the template exactly
Only replace the final xlsx file name

Template:
FD Reference - [Signoff Version|https://hkexgroup.sharepoint.com/:f:/r/sites/ProjectPortfolioMgt/PPM/Orion%20Derivatives%20Platform%20(ODP)/Project%20Documents/03%20Define_Design/Functional%20Specification/Clearing/Signoff%20Version?csf=1&web=1&e=YDzSok]Traceabiltiy Reference - {uploaded xlsx file name}
If the uploaded file name is:
R2.1-ODP Requirement Traceability Matrix_v1.0.1.xlsx
Then the fixed Description must be:
FD Reference - [Signoff Version|https://hkexgroup.sharepoint.com/:f:/r/sites/ProjectPortfolioMgt/PPM/Orion%20Derivatives%20Platform%20(ODP)/Project%20Documents/03%20Define_Design/Functional%20Specification/Clearing/Signoff%20Version?csf=1&web=1&e=YDzSok]Traceabiltiy Reference - R2.1-ODP Requirement Traceability Matrix_v1.0.1.xlsx

9. Leave-Blank Rules
Do not manually populate the following fields; keep them blank:

Issue key
Issue id
Created
Updated
Last Viewed
Resolved
Custom field (Rank)

Except for the fields that have been explicitly mapped or assigned fixed values above, all other fields without a defined source must remain blank. Do not guess values.

10. Validation Before Output
Before generating the CSV, please validate the following:

The header is exactly identical to the Jira sample CSV
No uncovered item remains
No empty Summary remains
No duplicate Business Requirement ID + Functional Requirement ID remains
The following fields must be non-empty:
Summary
Issue Type
Project key
Priority
Description
Reporter
Creator
Watchers
Custom field (BR ID)
Custom field (Business Requirement)
Custom field (Epic Link)
Custom field (FR ID)


11. Output File Naming Rule
Please name the output file using the following format:
Jira_Import_{original xlsx file name without extension}.csv
For example:
Jira_Import_R2.1-ODP Requirement Traceability Matrix_v1.0.1.csv

12. Execution Method
Please directly:

Read the uploaded files
Process the data
Generate the new CSV file
Return the download link

Only if critical mapping information is insufficient for safe generation (especially in scenarios where one file may map to multiple Epic Links), ask me the minimum necessary clarification question.