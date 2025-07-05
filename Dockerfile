FROM openjdk:17-jdk-slim

WORKDIR /app

COPY .mvn/ .mvn
COPY mvnw pom.xml ./

COPY src ./src

RUN ./mvnw package -DskipTests

EXPOSE 8080
EXPOSE 8000

ENTRYPOINT ["java", "-jar", "target/jobrunr-0.0.1-SNAPSHOT.jar"]
