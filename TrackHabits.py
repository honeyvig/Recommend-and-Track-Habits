import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QComboBox, QFileDialog
from PyQt5.QtCore import Qt
import datetime

class HealthTrackingApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the UI
        self.setWindowTitle("Health Tracking App: Frequency & Well-being")
        self.setGeometry(100, 100, 600, 400)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Introduction Label
        self.intro_label = QLabel("Track your health and wellness. Keep a record of your activities.", self)
        self.intro_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.intro_label)

        # Frequency ComboBox (Select frequency of activity)
        self.freq_label = QLabel("How often do you engage in the activity?")
        layout.addWidget(self.freq_label)

        self.frequency_combo = QComboBox(self)
        self.frequency_combo.addItem("Daily")
        self.frequency_combo.addItem("Weekly")
        self.frequency_combo.addItem("Monthly")
        self.frequency_combo.addItem("Occasionally")
        layout.addWidget(self.frequency_combo)

        # Direction ComboBox (Select the activity direction/steps)
        self.steps_label = QLabel("Select direction of steps or approach:")
        layout.addWidget(self.steps_label)

        self.steps_combo = QComboBox(self)
        self.steps_combo.addItem("Self-Relaxation")
        self.steps_combo.addItem("Exploration")
        self.steps_combo.addItem("Mindfulness")
        self.steps_combo.addItem("Meditation")
        layout.addWidget(self.steps_combo)

        # Gender Selection ComboBox
        self.gender_label = QLabel("Select Gender:")
        layout.addWidget(self.gender_label)

        self.gender_combo = QComboBox(self)
        self.gender_combo.addItem("Male")
        self.gender_combo.addItem("Female")
        layout.addWidget(self.gender_combo)

        # Record Button
        self.record_btn = QPushButton("Record Activity", self)
        self.record_btn.clicked.connect(self.record_activity)
        layout.addWidget(self.record_btn)

        # Recommendation Label
        self.recommendation_label = QLabel("Recommendations will be shown here.", self)
        self.recommendation_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.recommendation_label)

        # Set the layout
        self.setLayout(layout)

    def record_activity(self):
        # Retrieve selected data
        frequency = self.frequency_combo.currentText()
        steps = self.steps_combo.currentText()
        gender = self.gender_combo.currentText()

        # Get today's date
        today = datetime.date.today()

        # Log activity (just printing for now, could be saved to file or database)
        print(f"Date: {today}")
        print(f"Frequency: {frequency}")
        print(f"Steps: {steps}")
        print(f"Gender: {gender}")
        
        # Provide recommendation based on frequency and gender
        recommendation = self.generate_recommendation(frequency, steps, gender)
        self.recommendation_label.setText(recommendation)

    def generate_recommendation(self, frequency, steps, gender):
        # Basic logic to provide recommendations (to be customized)
        if frequency == "Daily":
            recommendation = "Daily activities may help with stress relief, but balance is key."
        elif frequency == "Weekly":
            recommendation = "Weekly activities help maintain a balanced approach."
        elif frequency == "Monthly":
            recommendation = "Monthly activity can be a good way to release tension."
        else:
            recommendation = "Occasional activities are fine, but don't forget to focus on other aspects of well-being."

        if gender == "Male":
            recommendation += "\nFor males, balance between relaxation and mindfulness is essential."
        elif gender == "Female":
            recommendation += "\nFor females, mindful practices and self-exploration are important."
        
        if steps == "Mindfulness":
            recommendation += "\nConsider incorporating deep breathing or meditation for enhanced relaxation."
        elif steps == "Meditation":
            recommendation += "\nMeditation can help enhance emotional balance and self-awareness."

        return recommendation


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = HealthTrackingApp()
    ex.show()
    sys.exit(app.exec_())
