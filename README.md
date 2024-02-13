# E-commerce Datasets

## 1. Parent Tables
   - **customers**: Contains information about customers such as their ID, name, email address, phone number, and address.
   - **products**: Contains information about products such as their ID, name, category, description, and price.

## 2. Child Tables Linked to Parent Tables
   - **orders**: Contains information about orders placed by customers, with a link to the customers table via the customer ID (`customer_id`) and the order details table via the order ID (`order_id`).
   - **order_details**: Contains detailed information about each product ordered within each order, with cross-references to the orders and products tables via the order ID (`order_id`) and product ID (`product_id`).

### Relationships between Tables
   - **customers** and **orders**: The `customer_id` column in the orders table is a foreign key that references the customer ID in the customers table. This establishes a one-to-many relationship where one customer can place multiple orders.
   - **orders** and **order_details**: The `order_id` column in the order_details table is a foreign key that references the order ID in the orders table. This establishes a one-to-many relationship where one order can contain multiple order details (i.e., products).
   - **order_details** and **products**: The `product_id` column in the order_details table is a foreign key that references the product ID in the products table. This establishes a many-to-one relationship where multiple order details (i.e., products) can be associated with one product.




# Transportation Datasets

## 1. Parent Tables
   - **locations**: Contains information about various transportation hubs such as cities, airports, and stations, including their ID, name, country, latitude, and longitude.
   - **vehicles**: Contains information about different types of vehicles used for transportation, including their ID, type (e.g., car, bus, train, airplane), capacity, and model.

## 2. Child Tables Linked to Parent Tables
   - **trips**: Contains information about individual trips or journeys, including the trip ID, origin and destination location IDs (linked to the locations table), vehicle ID (linked to the vehicles table), and start date.
   - **passengers**: Contains information about passengers traveling on specific trips, including the passenger ID, trip ID (linked to the trips table), passenger name, age, and origin (e.g., airport, bus station).

### Relationships between Tables
   - **locations** and **trips**: The `origin_location_id` and `destination_location_id` columns in the trips table are foreign keys that reference the location ID in the locations table. This establishes a many-to-one relationship where multiple trips can have the same origin or destination location.
   - **vehicles** and **trips**: The `vehicle_id` column in the trips table is a foreign key that references the vehicle ID in the vehicles table. This establishes a many-to-one relationship where multiple trips can be associated with the same vehicle.
   - **trips** and **passengers**: The `trip_id` column in the passengers table is a foreign key that references the trip ID in the trips table. This establishes a one-to-many relationship where one trip can have multiple passengers.



# Finance Datasets

## 1. Parent Tables
   - **customers**: Contains information about bank customers, including their ID, name, address, phone number, email, and social security number (masked for demonstration).
   - **accounts**: Contains information about customer accounts, including their ID, customer ID (linked to the customers table), account type (e.g., savings, checking, investment), and balance.

## 2. Child Tables Linked to Parent Tables
   - **transactions**: Contains information about financial transactions, including the transaction ID, account ID (linked to the accounts table), transaction type (e.g., deposit, withdrawal, transfer), amount, and date.
   - **investments**: Contains information about customer investments, including the investment ID, account ID (linked to the accounts table), symbol (investment symbol), shares, purchase price, and current price.

### Relationships between Tables
   - **customers** and **accounts**: The `customer_id` column in the accounts table is a foreign key that references the customer ID in the customers table. This establishes a one-to-many relationship where one customer can have multiple accounts.
   - **accounts** and **transactions**: The composite key `(account_id, transaction_id)` in the transactions table is a foreign key that references the account ID in the accounts table. This establishes a one-to-many relationship where one account can have multiple transactions.
   - **accounts** and **investments**: The composite key `(account_id, investment_id)` in the investments table is a foreign key that references the account ID in the accounts table. This establishes a one-to-many relationship where one account can have multiple investments.



# Education Datasets

## 1. Parent Tables
   - **students**: Contains information about students, including their ID, name, age, and grade level.
   - **courses**: Contains information about courses, including their ID, name, and subject.

## 2. Child Tables Linked to Parent Tables
   - **enrollments**: Contains information about student enrollments in courses, including the student ID (linked to the students table), course ID (linked to the courses table), and semester.
   - **grades**: Contains information about student grades in courses, including the enrollment ID (a unique identifier linking enrollments), student ID, course ID, and grade.

### Relationships between Tables
   - **students** and **enrollments**: The composite key `(student_id, course_id)` in the enrollments table is a foreign key that references the student ID in the students table. This establishes a many-to-many relationship where one student can enroll in multiple courses, and one course can have multiple students enrolled.
   - **courses** and **enrollments**: The composite key `(student_id, course_id)` in the enrollments table is a foreign key that references the course ID in the courses table. This establishes a many-to-many relationship where one course can have multiple enrollments, and one enrollment can belong to multiple courses.
   - **enrollments** and **grades**: The composite key `(student_id, course_id)` in the grades table is a foreign key that references the student ID and course ID in the enrollments table. This establishes a one-to-one relationship where one enrollment has one grade.



# Telecom Datasets

## 1. Parent Tables
   - **customers**: Contains information about mobile phone users, including their ID, name, phone number, address, and plan type.

## 2. Child Tables Linked to Parent Tables
   - **mobile_lines**: Contains information about mobile lines (subscriptions associated with phones), including the line ID (a unique identifier), customer ID (linked to the customers table), phone number, and activation date.
   - **calls**: Contains information about mobile voice calls between users, including the call ID (a unique identifier), calling line ID (linked to mobile_lines), called line ID (linked to mobile_lines), start time, and duration.
   - **sms**: Contains information about SMS messages (text messages between users), including the message ID (a unique identifier), sender line ID (linked to mobile_lines), recipient line ID (linked to mobile_lines), send time, and content.
   - **data_usage**: Contains information about data usage (internet data consumed by users), including the usage ID (a unique identifier), line ID (linked to mobile_lines), usage date, and data amount (in MB).

### Relationships between Tables
   - **customers** and **mobile_lines**: The customer ID in the mobile_lines table is a foreign key that references the customer ID in the customers table. This establishes a one-to-many relationship where one customer can have multiple mobile lines.
   - **mobile_lines** and **calls/sms/data_usage**: The line ID in the calls, sms, and data_usage tables is a foreign key that references the line ID in the mobile_lines table. This establishes a one-to-many relationship where one mobile line can have multiple associated calls, SMS messages, and data usage records.




# Real Estate Datasets

## 1. Parent Tables
   - **properties**: Contains information about properties (both residential and commercial), including their ID, type, address, city, state, zip code, number of bedrooms, number of bathrooms, square footage, year built, and price.

## 2. Child Tables Linked to Parent Tables
   - **listings**: Contains information about property listings (properties being offered for sale or rent), including the listing ID (a unique identifier), property ID (linked to properties), listing date, status (e.g., Active, Pending, Sold, Leased), list price, listing agent, and description.
   - **transactions**: Contains information about completed sales or rentals, including the transaction ID (a unique identifier), listing ID (linked to listings of sold properties), sale date, sale price, buyer name, and seller name.

### Relationships between Tables
   - **properties** and **listings**: The property ID in the listings table is a foreign key that references the property ID in the properties table. This establishes a one-to-many relationship where one property can have multiple listings.
   - **listings** and **transactions**: The listing ID in the transactions table is a foreign key that references the listing ID in the listings table. This establishes a one-to-many relationship where one listing can have multiple transactions (e.g., if a property is listed multiple times before being sold).




# Human Resource Datasets

## 1. Parent Tables
   - **employees**: Contains information about employees, including their ID, first name, last name, email, job title, hire date, address, and phone number.
   - **departments**: Contains information about departments, including their ID, name, location, and manager ID.

## 2. Child Tables Linked to Parent Tables
   - **salaries**: Contains information about employee salaries, including the salary ID (a unique identifier), employee ID (linked to employees), start date, and current salary.
   - **benefits**: Contains information about employee benefits, including the benefit ID (a unique identifier), employee ID (linked to employees), health insurance plan (e.g., PPO, HMO, HSA), and enrollment status.

### Relationships between Tables
   - **employees** and **departments**: The manager ID in the departments table is a foreign key that references the employee ID in the employees table. This establishes a one-to-many relationship where one employee can manage multiple departments.
   - **employees** and **salaries**: The employee ID in the salaries table is a foreign key that references the employee ID in the employees table. This establishes a one-to-many relationship where one employee can have multiple salary records (e.g., reflecting changes over time).
   - **employees** and **benefits**: The employee ID in the benefits table is a foreign key that references the employee ID in the employees table. This establishes a one-to-many relationship where one employee can have multiple benefit records (e.g., reflecting changes in enrollment).



# Government Services Datasets

## 1. Citizens Dataset
   - **CitizenID**: Unique identifier for each citizen.
   - **Name**: Name of the citizen.
   - **Age**: Age of the citizen.
   - **AddressID**: Foreign key referencing the AddressID in the Addresses dataset, indicating the citizen's address.
   - **TaxID**: Foreign key referencing the TaxID in the Taxes dataset, indicating the citizen's tax record.

## 2. Addresses Dataset
   - **AddressID**: Unique identifier for each address.
   - **Address**: Street address.
   - **City**: City of the address.
   - **State**: State of the address.
   - **ZipCode**: ZIP code of the address.

## 3. Taxes Dataset
   - **TaxID**: Unique identifier for each tax record.
   - **Year**: Year of the tax record.
   - **Amount**: Amount of taxes paid for the corresponding year.

### Relationships between Datasets
   - **Citizens** and **Addresses**: The AddressID in the Citizens dataset is a foreign key that references the AddressID in the Addresses dataset. This establishes a one-to-one relationship, indicating each citizen's address.
   - **Citizens** and **Taxes**: The TaxID in the Citizens dataset is a foreign key that references the TaxID in the Taxes dataset. This establishes a one-to-many relationship, indicating each citizen's tax records over time.



# Health Care Datasets

## 1. Patients Dataset
   - **patient_id**: Unique identifier for each patient.
   - **name**: Name of the patient.
   - **address**: Address of the patient.
   - **phone_number**: Phone number of the patient.
   - **email**: Email address of the patient.
   - **birth_date**: Date of birth of the patient.

## 2. Diagnoses Dataset
   - **diagnosis_id**: Unique identifier for each diagnosis.
   - **diagnosis_code**: Code representing the diagnosis.
   - **description**: Description of the diagnosis.

## 3. Prescriptions Dataset
   - **prescription_id**: Unique identifier for each prescription.
   - **patient_id**: Foreign key referencing the patient_id in the Patients dataset, indicating the patient receiving the prescription.
   - **medication**: Name of the prescribed medication.
   - **dosage**: Dosage of the medication.
   - **instructions**: Instructions for taking the medication.

## 4. Treatments Dataset
   - **treatment_id**: Unique identifier for each treatment.
   - **patient_id**: Foreign key referencing the patient_id in the Patients dataset, indicating the patient receiving the treatment.
   - **diagnosis_id**: Foreign key referencing the diagnosis_id in the Diagnoses dataset, indicating the diagnosis for the treatment.
   - **procedure**: Name of the treatment procedure.
   - **provider**: Name of the healthcare provider administering the treatment.
   - **date**: Date of the treatment.

### Relationships between Datasets
   - **Patients** and **Prescriptions**: The patient_id in the Prescriptions dataset is a foreign key that references the patient_id in the Patients dataset. This establishes a one-to-many relationship, indicating each patient's prescriptions.
   - **Patients** and **Treatments**: The patient_id in the Treatments dataset is a foreign key that references the patient_id in the Patients dataset. This establishes a one-to-many relationship, indicating each patient's treatments.
   - **Diagnoses** and **Treatments**: The diagnosis_id in the Treatments dataset is a foreign key that references the diagnosis_id in the Diagnoses dataset. This establishes a one-to-many relationship, indicating each diagnosis's treatments.



# Energy Datasets

## 1. Energy Consumption Dataset
   - **ConsumerID**: Unique identifier for each energy consumer.
   - **Location**: Location where energy consumption occurs.
   - **Usage_KWh**: Amount of energy consumed in kilowatt-hours (KWh).
   - **Month**: Month of the recorded energy consumption.
   - **Year**: Year of the recorded energy consumption.
   - **LocationID**: Unique identifier for each energy location.

## 2. Energy Production Dataset
   - **ProductionID**: Unique identifier for each energy production entry.
   - **Location**: Location where energy production occurs.
   - **Production_KWh**: Amount of energy produced in kilowatt-hours (KWh).
   - **Month**: Month of the recorded energy production.
   - **Year**: Year of the recorded energy production.
   - **LocationID**: Unique identifier for each energy location.

## 3. Energy Infrastructure Dataset
   - **FacilityID**: Unique identifier for each energy infrastructure facility.
   - **Location**: Location of the energy infrastructure facility.
   - **Type**: Type of energy infrastructure (e.g., Solar, Wind, Hydro, Nuclear).
   - **Capacity_MW**: Capacity of the energy infrastructure facility in megawatts (MW).
   - **LocationID**: Unique identifier for each energy location.

## 4. Energy Grid Dataset
   - **GridID**: Unique identifier for each energy grid entry.
   - **From**: Starting location of the energy transmission grid.
   - **To**: Destination location of the energy transmission grid.
   - **Distance_km**: Distance between the starting and destination locations in kilometers (km).
   - **Capacity_MW**: Capacity of the energy transmission grid in megawatts (MW).
   - **FromLocationID**:Unique identifier for each energy depart location.
   - **ToLocationID**: Unique identifier for each energy end location.

### Relationships between Datasets
   these datasets are linked based on common attribute locationId to analyze the interplay between energy consumption, production, infrastructure, and grid transmission.


# ERD SCHEMAS 

graph LR
    subgraph TELECOM
        A[Customers] --> B(line_id) | Mobile Lines
        B --> C(call_id) | Calls
        A --> B
        B --> C
        C[call_id] || calling_line_id | called_line_id
        B[line_id] || customer_id | number | activation_date
        A[Customers] || name | phone_number | address | plan
        C[call_id] || start_time | duration
        subgraph Data Usage
            D[Data Usage] --> B
            D[Data Usage] || usage_id | line_id | usage_date | data_amount
            B[line_id] || sender_line_id | recipient_line_id
        end
    end

    subgraph EDUCATION
        E[Students] --> F[enrollment_id] | Enrollments | semester
        F --> G[Courses] | Courses
        E --> F
        G --> F
        F[enrollment_id] || student_id | course_id
        E[Students] || student_id | name | age | grade_level
        G[Courses] || course_id | name | subject
        F[enrollment_id] || enrollment_id (PK)
    end

    subgraph E-COMMERCE
        H[Customers] --> I[order_id] | Orders | order_date
        I --> J[Products] | Products
        H --> I
        J --> I
        I[order_id] || order_id (PK) | customer_id | product_id | quantity
        H[Customers] || customer_id (PK) | name | email | phone_number | address
        J[Products] || product_id(PK) | name | category | description | price
        subgraph Order Detail
            I --> J
            I[order_id] || order_id (FK)
            J[Products] || product_id (FK)
        end
    end

    subgraph ENERGY
        K[Energy Consumption] --> L[LocationID] | Location
        K --> M[Energy Production] | Location
        L --> N[Energy Infrastructure] | Location
        M --> N | Location
        N --> O[Energy Grid] | FromLocationID | ToLocationID
        O --> P[Energy Infrastructure] | Location
        K[Energy Consumption] || ConsumerID (PK) | Location | Usage_KWh | Month | Year
        L[LocationID] || Address | City | State | ZipCode
        M[Energy Production] || ProductionID (PK) | Production_KWh | Month | Year
        N[Energy Infrastructure] || FacilityID (PK) | Type | Capacity_MW
        O[Energy Grid] || GridID (PK) | From | To | Distance_km | Capacity_MW
    end

    subgraph FINANCE
        Q[Customers] --> R[account_id] | Accounts
        R --> S[Transactions] | Transactions
        Q --> R
        R --> S
        S[Transactions] || transaction_id (PK) | account_id | transaction_type | amount | date
        Q[Customers] || customer_id (PK) | name | address | phone_number | email | social_security_nb
        R[account_id] || account_id (PK) | account_type | balance
        subgraph Investments
            R --> T[Investments]
            R[account_id] || account_id (FK)
            T[Investments] || investment_id (PK) | symbol | shares | purchase_price | current_price
        end
    end

    subgraph GOVERNMENT
        U[Addresses] --> V[CitizenID] | Citizens
        V --> W[Taxes] | Taxes
        U --> V
        W --> V
        V[CitizenID] || CitizenID(PK) | Name | Age
        U[Addresses] || AddressID (PK) | Address | City | State | ZipCode
        W[Taxes] || TaxID (PK) | Year | Amount
    end

    subgraph HEALTHCARE
        X[patients] --> Y[diagnoses] | diagnoses_code | description
        X --> Z[prescriptions] | medications | dosage | instructions
        X --> AA[treatments] | procedures | provider | date
        Y --> AA
        Z --> AA
        X[patients] || patient_id (PK) | name | address | phone_number | email | birth_date
        Y[diagnoses] || diagnosis_


