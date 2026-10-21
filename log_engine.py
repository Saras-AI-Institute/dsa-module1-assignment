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
        1. Split the string by the pipe '|' character using .split('|').
        2. Use a list comprehension or loop to strip accidental whitespaces from each piece (e.g., piece.strip()).
        3. Convert the cleaned list of pieces into a tuple: (timestamp, level, user_id, message)
        4. Append this tuple to self.logs_archive.
        5. Return the newly created tuple.
        """
        # HINT: 
        # parts = [item.strip() for item in raw_log.split('|')]
        # log_tuple = tuple(parts)
        
        # YOUR CODE HERE
        pass

    # =========================================================================
    # TASK 2: Unique Set Operations
    # =========================================================================
    def register_user(self, user_id: str) -> None:
        """
        TODO: Add the user_id to the self.unique_users set.
        (Remember: sets automatically handle duplicates for you!)
        """
        # YOUR CODE HERE
        pass

    def get_unique_user_count(self) -> int:
        """
        TODO: Return the total number of unique users seen by the system.
        (Hint: Use the built-in len() function on the set.)
        """
        # YOUR CODE HERE
        pass

    # =========================================================================
    # TASK 3: Map ADT / Dictionary Counting
    # =========================================================================
    def track_error_frequency(self, level: str, message: str) -> None:
        """
        TODO: If the log level is 'ERROR' or 'CRITICAL', record its frequency.
        1. Check if level is in ('ERROR', 'CRITICAL').
        2. If yes, use the 'message' string as the key in self.error_counts.
        3. Increment its count by 1 (handle the case where the key doesn't exist yet, 
           e.g., using dict.get(message, 0) + 1).
        If it's not an ERROR/CRITICAL log, do nothing.
        """
        # YOUR CODE HERE
        pass

    # =========================================================================
    # TASK 4: Advanced Thinking - Priority Queue ADT via List
    # =========================================================================
    def add_to_priority_alerts(self, log_tuple: tuple) -> None:
        """
        Severity mapping weight: 'CRITICAL' = 3, 'ERROR' = 2, 'WARNING' = 1.
        Any other level (like INFO or DEBUG) has a weight of 0 and should NOT be added.
        
        TODO: 
        1. Create a weight dictionary or map: {"CRITICAL": 3, "ERROR": 2, "WARNING": 1}
        2. Determine the weight of the log based on its level (log_tuple[1]).
        3. If weight > 0, append the log_tuple into self.priority_alerts.
        4. Keep the self.priority_alerts list sorted in DESCENDING order of weight at all times.
           (Hint: You can sort the list after appending using a custom key, e.g., 
            self.priority_alerts.sort(key=lambda x: weight_map[x[1]], reverse=True))
        """
        # YOUR CODE HERE
        pass

    def resolve_highest_priority_alert(self) -> tuple:
        """
        TODO: Remove and return the highest priority log alert from the 
        front/top of the queue (self.priority_alerts) so engineers can fix it.
        (Hint: Since the list is sorted with highest priority at the beginning, 
         you can use .pop(0)).
        Return None if the alerts list is empty.
        """
        # YOUR CODE HERE
        pass
