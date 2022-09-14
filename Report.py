################################################################################
# Take given News Project as Reference
#
# Report generation using the Decorator pattern
#
# Purpose: The classes in this module allow for reports to be generated.  The
# Decorator pattern is used: https://en.wikipedia.org/wiki/Decorator_pattern.

# The Report class defines the Component, the ReportBase class defines the
# ConcreteComponent that will be decorated (by default, all reports include
# the headlines from the associated source),
#
# ReportExtension defines the Decorator class, and ReportTitleSearch/ReportAllSearch define the
# ConcreteDecorator classes that "decorate" the report with additional
# information (results for searching for articles with a given term in the
# title of the articles, or in the entire article).
#
# We use the News API to access news data and produce news reports:
# - https://github.com/mattlisiv/newsapi-python
# - https://newsapi.org/docs
#
# Author: Qin Yang
# Contact: yangq90@mcmaster.ca
#
################################################################################

from app import *

# Defines what it means to be a report... must have a report_text method.  This
# is the "Component" in the Decorator pattern.


class Report(ABC):

    @abstractmethod
    def report_text(self):
        pass


# The base report will be a string of the top headlines for the given source.
# This corresponds to the ConcreteComponent of the Decorator pattern, it can
# optionally be decorated to extend the report contents.
class ReportBase(Report):

    # Calls News API to get top headlines, puts headline data into a string
    def report_text(self):
        headlines = APP().newsapi.get_top_headlines(sources=self.__currency_type)
        report_text = "Headlines from " + self.__currency_type+ "\n\n"
        for article in headlines["articles"]:
            report_text = report_text + \
                          "Title: " + str(article["title"]) + "\n" + \
                          "Description: " + str(article["description"]) + "\n\n"
        return report_text

    def __init__(self, currency_type):
        self.__currency_type = currency_type


# Extensions to the report will involve a search term, this defines what it
# means to be an extension.  Extension would me holding time opinion
# This class corresponds to the Decorator class in the Decorator pattern.
class ReportExtension(Report):

    def __init__(self, report, currency_type, holding_time_option):
        self.report = report
        self.currency_type = currency_type
        self.holding_time_option = holding_time_option
