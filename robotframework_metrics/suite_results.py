from robot.api import ResultVisitor
from robot.utils.markuputils import html_format

SUITE_ORDER = 0

class SuiteResults(ResultVisitor):

    def __init__(self, suite_list):
        self.suite_list = suite_list
    
    def start_suite(self, suite):
        if suite.tests:
            global SUITE_ORDER
            SUITE_ORDER += 1
            try:
                stats = suite.statistics.all
            except:
                stats = suite.statistics
            
            try:
                skipped = stats.skipped
            except:
                skipped = 0

            suite_json = {
                "Order" : SUITE_ORDER,
                "Name" : suite.longname,
                "Id" : suite.id,
                "Status" : suite.status,
                "Documentation" : html_format(suite.doc),
                "Total" : stats.total,
                "Pass" : stats.passed,
                "Fail" : stats.failed,
                "Skip" : skipped,
                "Time" : suite.elapsedtime,
            }
            self.suite_list.append(suite_json)