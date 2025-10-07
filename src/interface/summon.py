from src.registry.function_registry import FunctionRegistry

def summon_interface():
    registry = FunctionRegistry()

    print("🧬 Cyberdna Summoning Interface")
    print("Type 'list' to view functions, 'summon [ID]' to call, 'edit [ID]' to update, or 'exit' to leave.\n")

    while True:
        command = input(">> ").strip()

        if command == "exit":
            print("Closing the altar. Invocation complete.")
            break

        elif command == "list":
            functions = registry.list_functions()
            for segment_id, title in functions.items():
                print(f"{segment_id}: {title}")

        elif command.startswith("summon "):
            segment_id = command.split(" ", 1)[1]
            func = registry.summon(segment_id)
            if func:
                print(f"\n🔹 Summoning {segment_id} — {func['title']}")
                print(f"Traits: {func['traits']}")
                print(f"Code:\n{func['code']}\n")
            else:
                print("⚠️ Function not found.")

        elif command.startswith("edit "):
            segment_id = command.split(" ", 1)[1]
            func = registry.summon(segment_id)
            if func and func["editable"]:
                print(f"Editing {segment_id} — {func['title']}")
                new

