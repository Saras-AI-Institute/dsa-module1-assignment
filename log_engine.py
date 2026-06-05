"""
Loglytics: Module 1 DSA Assignment
Name: [STUDENT NAME]
Roll Number: [STUDENT ID]
"""

class LoglyticsEngine:
    def __init__(self):
        # Task 1 Storage: List to hold all parsed log tuples
        self.logs_archive = []
        
        # Task 2 Storage: Track unique user IDs
        self.unique_users = set()
        
        # Task 3 Storage: Map to track frequency of specific error messages
        self.error_counts = {}
        
        # Task 4 Storage: Priority Queue representation using a list
        self.priority_alerts = []

    # =========================================================================
    # TASK 1: String Parsing & Tuple Immutable Storage
    # =========================================================================
    def parse_and_archive_log(self, raw_log: str) -> tuple:
        """
        Receives a raw log line, cleans it, and archives it.
        Raw format: "TIMESTAMP | LEVEL | USER_ID | MESSAGE"
        Example: "14:05:32 | ERROR | user_404 | Connection dropped"
        
        TODO: 
        1. Split the string by the pipe '|' character.
        2. Strip any accidental leading/trailing whitespaces from each piece.
        3. Convert the pieces into a tuple: (timestamp, level, user_id, message)
        4. Append this tuple to self.logs_archive.
        5. Return the newly created tuple.
        """
        # YOUR CODE HERE
        pass

    # =========================================================================
    # TASK 2: Unique Set Operations
    # =========================================================================
    def register_user(self, user_id: str) -> None:
        """
        TODO: Add the user_id to the self.unique_users set.
        """
        # YOUR CODE HERE
        pass

    def get_unique_user_count(self) -> int:
        """
        TODO: Return the total number of unique users seen by the system.
        """
        # YOUR CODE HERE
        pass

    # =========================================================================
    # TASK 3: Map ADT / Dictionary Counting
    # =========================================================================
    def track_error_frequency(self, level: str, message: str) -> None:
        """
        TODO: If the log level is 'ERROR' or 'CRITICAL', record its frequency.
        Use the 'message' string as the key in self.error_counts dictionary, 
        and increment its count value by 1 every time it is encountered.
        If it's not an ERROR/CRITICAL log, do nothing.
        """
        # YOUR CODE HERE
        pass

    # =========================================================================
    # TASK 4: Advanced Thinking - Priority Queue ADT via List
    # =========================================================================
    def add_to_priority_alerts(self, log_tuple: tuple) -> None:
        """
        We need to sort our highest-priority logs. 
        Severity mapping weight: 'CRITICAL' = 3, 'ERROR' = 2, 'WARNING' = 1.
        Any other level (like INFO or DEBUG) has a weight of 0 and should NOT be added.
        
        TODO: 
        1. Determine the weight of the log based on its level (log_tuple[1]).
        2. If weight > 0, insert the log_tuple into self.priority_alerts.
        3. CRITICAL THINKING STEP: Keep the self.priority_alerts list sorted 
           in DESCENDING order of weight at all times. 
           (If weights are equal, the order of insertion does not matter).
        
        Example state of list: [ (t1, 'CRITICAL',...), (t2, 'ERROR',...), (t3, 'WARNING',...) ]
        """
        # YOUR CODE HERE
        pass

    def resolve_highest_priority_alert(self) -> tuple:
        """
        TODO: Remove and return the highest priority log alert from the 
        front/top of the queue (self.priority_alerts) so engineers can fix it.
        Return None if the alerts list is empty.
        """
        # YOUR CODE HERE
        pass
