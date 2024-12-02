from py2neo import Graph


graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

def create_knowledge_graph(entities, relationships, properties):
    # Create nodes for entities
    for entity_type, entity_list in entities.items():
        for entity in entity_list:
            graph.run(f"MERGE (e:{entity_type} {{name: '{entity}'}})")

    
    for rel in relationships:
        graph.run(f"""
            MATCH (a:{rel['subject']}), (b:{rel['object']})
            MERGE (a)-[r:{rel['relationship']}]->(b)
        """)

  
    for entity_type, entity_list in entities.items():
        for entity in entity_list:
            for property, value in properties.items():
                graph.run(f"""
                    MATCH (e:{entity_type} {{name: '{entity}'}})
                    SET e.{property} = '{value}'
                """)
