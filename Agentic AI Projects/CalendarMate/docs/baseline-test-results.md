# Baseline Test Results --- T1 to T12

The supplied evaluation artifacts report **12/12 baseline tests passed**
with no hallucination anomalies detected.

  ---------------------------------------------------------------------------
  ID                Test Input          Expected Behavior   Reported Result
  ----------------- ------------------- ------------------- -----------------
  T1                What does my day    List today's        PASS
                    look like today?    meetings with       
                                        times/attendees;    
                                        mention conflicts   

  T2                Give me a summary   List tomorrow's     PASS
                    of my meetings for  meetings; do not    
                    tomorrow.           invent              

  T3                Schedule a          Check availability; PASS
                    30-minute meeting   create event with   
                    with                Meet link; confirm  
                    sarah@company.com                       
                    tomorrow at 2pm.                        

  T4                Set up a sync with  Ask                 PASS
                    the design team     day/time/attendee   
                    sometime this week. clarification; do   
                                        not book            

  T5                Find a time for a   Check availability; PASS
                    1-hour meeting with propose slots       
                    john@ext.com and                        
                    lisa@ext.com next                       
                    Monday.                                 

  T6                Schedule something  Flag                PASS
                    for Sunday at 6am.  weekend/unusual     
                                        hour; request       
                                        confirmation/warn   

  T7                Summarize my unread Group by            PASS
                    emails.             urgency/topic;      
                                        separate action/FYI 

  T8                What emails need my Return              PASS
                    attention today?    action-required     
                                        emails with         
                                        sender/subject      

  T9                Book a meeting but  Ask for attendee;   PASS
                    I forgot with whom. do not create       

  T10               Do I have any       Check week for      PASS
                    conflicts this      overlaps; list      
                    week?               conflicts or none   

  T11               Schedule a meeting  Detect conflict;    PASS
                    at the same time as warn; suggest       
                    my existing         alternatives        
                    standup.                                

  T12               What's happening    Show only next      PASS
                    next Thursday?      Thursday's events   
  ---------------------------------------------------------------------------

## Evaluation Summary

-   **Tests:** 12
-   **Passed:** 12
-   **Failed:** 0
-   **Reported hallucination anomalies:** 0

## Edge Cases Reported

-   Empty calendar day.
-   Past-date scheduling.
-   Vague email request.

## Prompt Modification Findings

The supplied results report that explicit grounding instructions reduced
an early failure mode involving inferred meeting details, and that
routing instructions were tightened to reduce scheduler/follow-up
misrouting.

> The full visual evidence is preserved under `evidence/` and `images/`.
