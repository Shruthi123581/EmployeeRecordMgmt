import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
import csv

# Define a dictionary to store employee time data
time_data = {}


# Define a function to record the employee's clock-in and clock-out times
def record_time(employee_id, action):
    # Get the current date and time
    now = datetime.datetime.now()
    # Format the date and time as a string
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    # Update the time data dictionary
    if employee_id not in time_data:
        time_data[employee_id] = {"entries": [], "total_hours": 0}
    time_data[employee_id]["entries"].append((current_time, action))
    # Calculate total hours worked
    if len(time_data[employee_id]["entries"]) >= 2:
        clock_in_time = datetime.datetime.strptime(time_data[employee_id]["entries"][-2][0], "%Y-%m-%d %H:%M:%S")
        clock_out_time = datetime.datetime.strptime(time_data[employee_id]["entries"][-1][0], "%Y-%m-%d %H:%M:%S")
        time_difference = clock_out_time - clock_in_time
        hours_worked = time_difference.total_seconds() / 3600
        time_data[employee_id]["total_hours"] += hours_worked


# Define a function to save the time data as a CSV file
def save_time_data():
    with open('time_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        for employee_id in time_data:
            for time_entry in time_data[employee_id]["entries"]:
                writer.writerow([employee_id, time_entry[0], time_entry[1], time_data[employee_id]["total_hours"]])


def save_time_data_view(request):
    # Define the content type of the response
    response = HttpResponse(content_type='text/csv')
    # Set the filename of the CSV file to be downloaded
    response['Content-Disposition'] = 'attachment; filename="time_data.csv"'
    # Write the time data to a CSV file
    writer = csv.writer(response)
    for employee_id in time_data:
        for time_entry in time_data[employee_id]["entries"]:
            writer.writerow([employee_id, time_entry[0], time_entry[1], time_data[employee_id]["total_hours"]])
    # Return the CSV file as the response
    return response


def show_time_data(request):
    # Read the time data from the CSV file
    time_data = {}
    with open('time_data.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            employee_id, time_entry, action, total_hours = row
            if employee_id not in time_data:
                time_data[employee_id] = {"entries": [], "total_hours": float(total_hours)}
            time_data[employee_id]["entries"].append((time_entry, action))
    # Pass the time data to a template for rendering
    context = {'time_data': time_data}
    return render(request, 'time_data.html', context)


# Define a view function for the employee time tracker page
def time_tracker(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        action = request.POST.get('action')
        if not employee_id:
            context = {'status': "Please enter an employee ID.", 'color': "red"}
        elif action == "clock in":
            if employee_id in time_data and time_data[employee_id]["entries"][-1][1] == "clock in":
                context = {'status': "You are already clocked in.", 'color': "red"}
            else:
                record_time(employee_id, "clock in")
                context = {'status': "You are now clocked in.", 'color': "green"}
        elif action == "clock out":
            if employee_id not in time_data or time_data[employee_id]["entries"][-1][1] == "clock out":
                context = {'status': "You are not clocked in.", 'color': "red"}
            else:
                record_time(employee_id, "clock out")
                context = {'status': "You are now clocked out.", 'color': "green"}
                # Save the time data to a CSV file
                save_time_data()
    else:
        context = {}
    return render(request, 'time_tracker.html', context)

