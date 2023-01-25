from solution import generate_schema_from_file


def run_program():
    source_file = input("Enter source file: ")
    output_file = input("Enter output filename without extension: ")
    saved_schema_file = generate_schema_from_file(source_file=source_file, output_file=output_file)
    print(saved_schema_file)


if __name__ == '__main__':
    print("Running program")
    run_program()
