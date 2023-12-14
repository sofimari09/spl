"""
Diagram Service Module

This module provides a service for creating various diagrams based
on user data using the `matplotlib` library.

Usage:
1. Import the module: `from matplotlib import pyplot as plt`
2. Create an instance of `DiagramServiceImpl` with user data.
3. Use the provided methods to retrieve data and create diagrams.

Note: Ensure the required libraries (`matplotlib`) are installed before using this module.
You can install it using: `pip install matplotlib`

Example:
```python
from src.service.lab8.diagrams_service import DiagramServiceImpl

# Create an instance of DiagramServiceImpl with a file path
diagram_service = DiagramServiceImpl("path/to/user_data.csv")

# Create and display diagrams
diagram_service.create_difference_in_years_histogram()
diagram_service.create_sex_pie_chart()
diagram_service.create_job_bar_chart()
diagram_service.create_combined_diagram()
"""
from collections import Counter
import abc
from matplotlib import pyplot as plt
from config.paths_config import (DIFFERENCE_IN_YEARS_HISTOGRAM, SEX_PIE_CHART_PHOTO,
                                 JOB_BAR_CHART_PHOTO, COMBINED_DIAGRAM_PHOTO)
from  config.logger_config import logger
from entity.user import User
from shared.data_processor import DateProcessor
from shared.file_processors import CsvProcessor as csv_processor


class DiagramService(abc.ABC):
    """
    Abstract base class for creating diagrams based on user data.

    Attributes:
        _users (list): List to store User objects.

    Methods:
        __init__.py: Initializes the DiagramService object.

    Subclasses must implement their own methods for data retrieval and diagram creation.
    """

    def __init__(self):
        """
        Abstract base class for creating diagrams based on user data.

        Attributes:
            _users (list): List to store User objects.

        Methods:
            __init__.py: Initializes the DiagramService object.

        Subclasses must implement their own methods for data retrieval and diagram creation.
        """
        self._users = []


class DiagramServiceImpl(DiagramService):
    """
    Implementation class for creating diagrams based on user data.

    Attributes:
        _users (list): List to store User objects.

    Methods:
        __init__.py: Initializes the DiagramServiceImpl object with user data.
        get_difference_in_years: Retrieves the age difference for each user.
        get_sex: Retrieves the sex of each user.
        get_job_title: Retrieves the job title of each user.
        create_difference_in_years_histogram: Creates a histogram of age differences.
        create_sex_pie_chart: Creates a pie chart of user sexes.
        create_job_bar_chart: Creates a bar chart of job titles.
        create_combined_diagram: Creates a combined diagram with job frequency and age histogram.
    """

    def __init__(self, file_path: str):
        super().__init__()
        users_dataframe = csv_processor.read(file_path)
        for data in users_dataframe.values:
            self._users.append(User(data))

    def get_difference_in_years(self):
        """
       Retrieve the age difference for each user.

       Returns:
           List[int]: List of age differences.
       """
        return [DateProcessor.calculate_year_difference(user.date_of_birth) for user in self._users]

    def get_sex(self):
        """
       Retrieve the sex of each user.

       Returns:
           List[str]: List of user sexes.
       """
        return [user.sex for user in self._users]

    def get_job_title(self):
        """
        Retrieve the job title of each user.

        Returns:
            List[str]: List of user job titles.
        """
        logger.info("Retrieving job titles")
        return [user.job_title for user in self._users]

    def create_difference_in_years_histogram(self, has_to_be_downloaded=False):
        """
        Create and display a histogram of age differences.

        Parameters:
            has_to_be_downloaded (bool): Flag to determine if the diagram should be downloaded.

        Returns:
            None
        """
        difference_in_years = self.get_difference_in_years()
        plt.hist(difference_in_years,
                 bins=range(min(difference_in_years), max(difference_in_years)), edgecolor='black')
        if has_to_be_downloaded:
            plt.savefig(DIFFERENCE_IN_YEARS_HISTOGRAM)

        plt.title('Histogram')
        plt.xlabel('Age')
        plt.ylabel('Frequency')

        plt.show()

    def create_sex_pie_chart(self, has_to_be_downloaded=False):
        """
        Create and display a pie chart of user sexes.

        Parameters:
            has_to_be_downloaded (bool): Flag to determine if the diagram should be downloaded.

        Returns:
            None
        """
        sex = self.get_sex()
        sex_counter = Counter(sex)

        plt.pie(list(sex_counter.values()), labels=list(sex_counter), startangle=90,
                colors=['blue', 'pink'])

        if has_to_be_downloaded:
            plt.savefig(SEX_PIE_CHART_PHOTO)

        plt.title('Pie Chart')
        plt.show()

    def create_job_bar_chart(self, has_to_be_downloaded=False):
        """
        Create and display a bar chart of job titles.

        Parameters:
            has_to_be_downloaded (bool): Flag to determine if the diagram should be downloaded.

        Returns:
            None
        """
        job_title = self.get_job_title()
        job_title_counter = Counter(job_title)

        plt.figure(figsize=(11, 16))
        plt.bar(list(job_title_counter), list(job_title_counter.values()), color='green')

        if has_to_be_downloaded:
            plt.savefig(JOB_BAR_CHART_PHOTO)
        plt.title('Bar Chart')
        plt.xlabel('Job')
        plt.ylabel('Frequency')
        plt.xticks(fontsize=6)  # You can adjust the font size here
        plt.yticks(fontsize=10)
        plt.xticks(rotation=-90)

        plt.show()

    def create_combined_diagram(self, has_to_be_downloaded=False):
        """
       Create and display a combined diagram with job frequency and age histogram.

       Parameters:
           has_to_be_downloaded (bool): Flag to determine if the diagram should be downloaded.

       Returns:
           None
       """
        job_title = self.get_job_title()
        job_title_counter = Counter(job_title)
        difference_in_years = self.get_difference_in_years()

        # Create a figure with two subplots
        _, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 16))

        # First subplot (bar chart)
        ax1.bar(list(job_title_counter), list(job_title_counter.values()), color='green')

        ax1.set_title('Job Frequency')
        ax1.set_xlabel('Job')
        ax1.set_ylabel('Frequency')
        ax1.tick_params(axis='x', labelrotation=-90)
        ax1.tick_params(axis='x', labelsize=6)
        ax1.tick_params(axis='y', labelsize=10)

        # Second subplot (histogram)
        ax2.hist(difference_in_years, bins=range(min(difference_in_years),
                                                 max(difference_in_years)), edgecolor='black')
        ax2.set_title('Difference in Years Histogram')
        ax2.set_xlabel('Age')
        ax2.set_ylabel('Frequency')

        # Adjust layout to prevent overlapping
        plt.tight_layout()

        # Save figures if needed
        if has_to_be_downloaded:
            plt.savefig(COMBINED_DIAGRAM_PHOTO)

        # Display the plot
        plt.show()
