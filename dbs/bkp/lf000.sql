--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3
-- Dumped by pg_dump version 15.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: client; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.client (
    id integer NOT NULL,
    name text NOT NULL,
    addresses text[],
    phones text[],
    emails text[],
    observation text,
    cpf text,
    cnpj text,
    status integer
);


ALTER TABLE public.client OWNER TO postgres;

--
-- Name: client_status; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.client_status (
    id integer NOT NULL,
    description text NOT NULL
);


ALTER TABLE public.client_status OWNER TO postgres;

--
-- Name: lawsuit; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.lawsuit (
    id integer NOT NULL,
    cnj character(20) NOT NULL,
    status integer,
    observation text
);


ALTER TABLE public.lawsuit OWNER TO postgres;

--
-- Name: lawsuit_status; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.lawsuit_status (
    id integer NOT NULL,
    description text NOT NULL
);


ALTER TABLE public.lawsuit_status OWNER TO postgres;

--
-- Name: lawyers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.lawyers (
    id integer NOT NULL,
    name text NOT NULL,
    addresses text[],
    phones text[],
    emails text[],
    cpf text,
    cnpj text,
    status integer,
    observation text
);


ALTER TABLE public.lawyers OWNER TO postgres;

--
-- Name: lawyers_status; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.lawyers_status (
    id integer NOT NULL,
    name text NOT NULL
);


ALTER TABLE public.lawyers_status OWNER TO postgres;

--
-- Name: logs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.logs (
    id integer NOT NULL,
    user_id integer NOT NULL,
    action_date timestamp without time zone NOT NULL,
    table_type_id integer NOT NULL,
    field text NOT NULL,
    prev_value text NOT NULL,
    current_value text NOT NULL,
    logs_type_id integer NOT NULL
);


ALTER TABLE public.logs OWNER TO postgres;

--
-- Name: logs_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.logs_type (
    id integer NOT NULL,
    type text NOT NULL
);


ALTER TABLE public.logs_type OWNER TO postgres;

--
-- Name: profiles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.profiles (
    id integer NOT NULL,
    name text NOT NULL,
    permissions text[],
    status integer NOT NULL
);


ALTER TABLE public.profiles OWNER TO postgres;

--
-- Name: profiles_status; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.profiles_status (
    id integer NOT NULL,
    name text NOT NULL
);


ALTER TABLE public.profiles_status OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username text NOT NULL,
    password text NOT NULL,
    status integer NOT NULL,
    profile integer NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_status; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users_status (
    id integer NOT NULL,
    name text NOT NULL
);


ALTER TABLE public.users_status OWNER TO postgres;

--
-- Data for Name: client; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.client (id, name, addresses, phones, emails, observation, cpf, cnpj, status) FROM stdin;
\.


--
-- Data for Name: client_status; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.client_status (id, description) FROM stdin;
\.


--
-- Data for Name: lawsuit; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.lawsuit (id, cnj, status, observation) FROM stdin;
\.


--
-- Data for Name: lawsuit_status; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.lawsuit_status (id, description) FROM stdin;
\.


--
-- Data for Name: lawyers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.lawyers (id, name, addresses, phones, emails, cpf, cnpj, status, observation) FROM stdin;
\.


--
-- Data for Name: lawyers_status; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.lawyers_status (id, name) FROM stdin;
\.


--
-- Data for Name: logs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.logs (id, user_id, action_date, table_type_id, field, prev_value, current_value, logs_type_id) FROM stdin;
\.


--
-- Data for Name: logs_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.logs_type (id, type) FROM stdin;
\.


--
-- Data for Name: profiles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.profiles (id, name, permissions, status) FROM stdin;
\.


--
-- Data for Name: profiles_status; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.profiles_status (id, name) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, username, password, status, profile) FROM stdin;
\.


--
-- Data for Name: users_status; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users_status (id, name) FROM stdin;
\.


--
-- Name: client client_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.client
    ADD CONSTRAINT client_pkey PRIMARY KEY (id);


--
-- Name: client_status client_status_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.client_status
    ADD CONSTRAINT client_status_pkey PRIMARY KEY (id);


--
-- Name: lawsuit lawsuit_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lawsuit
    ADD CONSTRAINT lawsuit_pkey PRIMARY KEY (id);


--
-- Name: lawsuit_status lawsuit_status_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lawsuit_status
    ADD CONSTRAINT lawsuit_status_pkey PRIMARY KEY (id);


--
-- Name: lawyers lawyers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lawyers
    ADD CONSTRAINT lawyers_pkey PRIMARY KEY (id);


--
-- Name: lawyers_status lawyers_status_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lawyers_status
    ADD CONSTRAINT lawyers_status_pkey UNIQUE (id);


--
-- Name: logs logs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.logs
    ADD CONSTRAINT logs_pkey UNIQUE (id);


--
-- Name: profiles profiles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.profiles
    ADD CONSTRAINT profiles_pkey UNIQUE (id);


--
-- Name: profiles_status profiles_status_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.profiles_status
    ADD CONSTRAINT profiles_status_pkey UNIQUE (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users_status users_status_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_status
    ADD CONSTRAINT users_status_pkey UNIQUE (id);


--
-- PostgreSQL database dump complete
--

